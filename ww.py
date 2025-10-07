import time
import serial
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
        detected_encoding = chardet.detect(response)['encoding'] or 'utf-8'
        print(f"Detected encoding: {detected_encoding}")
        return response.hex()

    def receive_data(self, num_bytes):
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        data = self.serial_conn.read(num_bytes)
        return data.hex()

    def set_input_signal(self, signal_name, value, duration=1):
        if signal_name not in self.input_signal_map:
            raise ValueError(f"Unknown input signal name: {signal_name}")
        signal_id = self.input_signal_map[signal_name]
        self.active_signals[signal_name] = value

        if value == 1:
            self.send_integer_data(signal_id)
            self.send_integer_data(value)
            self.blink_flags[signal_name] = True
            print(f"Set input signal '{signal_name}' to {value}")

            end_time = time.time() + duration
            while time.time() < end_time:
                self.send_integer_data(signal_id)
                self.send_integer_data(value)
                time.sleep(1)

            self.send_integer_data(signal_id)
            self.send_integer_data(0)
            self.blink_flags[signal_name] = False
            print(f"Reset input signal '{signal_name}' after {duration} seconds")
        else:
            print(f"Input signal '{signal_name}' is set to 0, no command sent.")

    def get_output_signal(self, signal_name):
        if signal_name not in self.output_signal_map:
            raise ValueError(f"Unknown output signal name: {signal_name}")
        signal_id = self.output_signal_map[signal_name]
        self.send_integer_data(signal_id)
        response = self.read_response()
        print(f"Output signal '{signal_name}' value: {response}")
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
            "Set_wiper": 201,
            "Set_washer": 202,
        }

    def _generate_output_signal_map(self):
        return {
            "Wiper_Status": 211,
            "Washer_Status": 212,
        }


if __name__ == "__main__":
    hil = HILSimulator(com_port="COM13")
    try:
        hil.connect()

        # Activate wiper for 3 seconds
        hil.set_input_signal("Set_wiper", 1, duration=3)
        print("Wiper Status:", hil.get_output_signal("Wiper_Status"))

        # Activate washer for 2 seconds
        hil.set_input_signal("Set_washer", 1, duration=2)
        print("Washer Status:", hil.get_output_signal("Washer_Status"))

        # Read raw response from HIL
        raw_data = hil.receive_data(10)
        print(f"Received raw data: {raw_data}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        hil.disconnect()
