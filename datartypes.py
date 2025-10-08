import time
import serial  # For COM port communication
import chardet

class HILSimulator:
    def __init__(self, com_port, baudrate=115200, timeout=1):
        self.com_port = com_port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.input_signal_map = self._generate_input_signal_map()
        self.output_signal_map = self._generate_output_signal_map()
        self.active_signals = {}
        self.blink_flags = {}

    def connect(self):
        try:
            self.serial_conn = serial.Serial(self.com_port, baudrate=self.baudrate, timeout=self.timeout)
            print(f"Connected to HIL simulator on {self.com_port}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to {self.com_port}: {e}")

    def disconnect(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            print("Disconnected from HIL simulator.")

    def send_command(self, command):
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        self.serial_conn.write(command.encode('ISO-8859-1') + b'\n')
        time.sleep(0.1)

    def read_response(self):
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        response = self.serial_conn.readline()
        detected_encoding = chardet.detect(response)['encoding']
        if not detected_encoding or detected_encoding.lower() == 'ascii':
            detected_encoding = 'utf-8'
        print(f"Detected encoding: {detected_encoding}")
        hex_response = response.hex()
        return hex_response

    def receive_data(self, num_bytes):
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        data = self.serial_conn.read(num_bytes)
        hex_data = data.hex()
        return hex_data

    def set_input_signal(self, signal_name, value, duration=1):
        if signal_name not in self.input_signal_map:
            raise ValueError(f"Unknown input signal name: {signal_name}")
        signal_id = self.input_signal_map[signal_name]
        self.active_signals[signal_name] = value

        if value == 1:
            self.send_integer_data(signal_id)
            self.send_integer_data(value)
            self.blink_flags[signal_name] = True
            print(f"Set input signal '{signal_name}' (ID: {signal_id}) to value: {value}")

            # Send the signal for the specified duration
            end_time = time.time() + duration
            while time.time() < end_time:
                self.send_integer_data(signal_id)
                self.send_integer_data(value)
                time.sleep(1)  # Adjust this sleep time if needed

            # Reset the signal after the duration
            self.send_integer_data(signal_id)
            self.send_integer_data(0)
            self.blink_flags[signal_name] = False
            print(f"Reset input signal '{signal_name}' (ID: {signal_id}) after {duration} seconds")
        else:
            print(f"Input signal '{signal_name}' is set to 0, no command sent.")

    def maintain_signals(self):
        while True:
            for signal_name, value in self.active_signals.items():
                if value == 1 and self.blink_flags.get(signal_name, False):
                    signal_id = self.input_signal_map[signal_name]
                    self.send_integer_data(signal_id)
                    self.send_integer_data(1)
                    print(f"Blinking input signal '{signal_name}' (ID: {signal_id}) - ON")
                    time.sleep(0.5)
                    self.send_integer_data(signal_id)
                    self.send_integer_data(0)
                    print(f"Blinking input signal '{signal_name}' (ID: {signal_id}) - OFF")
                    time.sleep(0.5)
            time.sleep(1)

    def get_output_signal(self, signal_name):
        if signal_name not in self.output_signal_map:
            raise ValueError(f"Unknown output signal name: {signal_name}")
        signal_id = self.output_signal_map[signal_name]
        self.send_integer_data(signal_id)
        response = self.read_response()
        print(f"Retrieved output signal '{signal_name}' (ID: {signal_id}): {response}")
        return response

    def send_integer_data(self, data):
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        self.serial_conn.write(data.to_bytes(4, byteorder='little', signed=True))
        print(f"Sent integer data: {data}")

    def _generate_input_signal_map(self):
        return {
            "Set_left_direction": 101,
            "Set_right_direction": 102,
            "Set_Hazard_indicator": 103,
        }

    def _generate_output_signal_map(self):
        return {
            "Dir_Ind_Li_inp": 111,
            "Hz_Li_Inp": 111,
        }


# Example usage
if __name__ == "__main__":
    hil = HILSimulator(com_port="COM13")
    try:
        hil.connect()

        # Example: Set right direction for 10 seconds
        hil.set_input_signal("Set_left_direction", 1, duration=3)
        response = hil.get_output_signal("Dir_Ind_Li_inp")
        print(f"Dir_Ind_Li_inp: {response}")

        # Example: Receive raw data from the HIL simulator
        raw_data = hil.receive_data(8)  # Receive 10 bytes of data
        print(f"Received direction inp sts: {raw_data}")

        # Example: Set Low Beam and validate its status
        hil.set_input_signal("Set_right_direction", 0, duration=4)  # Turn on Low Beam
        response = hil.get_output_signal("Dir_Ind_Li_inp")
        print(f"Dir_Ind_Li_inp: {response}")

        # Example: Receive raw data from the HIL simulator
        raw_data = hil.receive_data(10)  # Receive 10 bytes of data
        print(f"Received direction inp sts: {raw_data}")

        # Example: Set Hazard Indicator and validate its status
        hil.set_input_signal("Set_Hazard_indicator", 0, duration=1)  # Turn on hazard Beam
        response = hil.get_output_signal("Hz_Li_Inp")
        print(f"Hz_Li_Inp: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        hil.disconnect()

