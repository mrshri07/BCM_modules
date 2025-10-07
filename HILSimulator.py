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

    def send_integer_data(self, data):
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection to the HIL simulator.")
        self.serial_conn.write(data.to_bytes(4, byteorder='little', signed=True))
        print(f"Sent integer data: {data}")

    def get_output_signal(self, signal_name):
        if signal_name not in self.output_signal_map:
            raise ValueError(f"Unknown output signal name: {signal_name}")
        signal_id = self.output_signal_map[signal_name]
        self.send_integer_data(signal_id)
        response = self.read_response()
        print(f"Retrieved output signal '{signal_name}' (ID: {signal_id}): {response}")
        return response

    def _generate_input_signal_map(self):
        return {
            "Wiper_Int": 201,
            "Wiper_Low": 202,
            "Wiper_High": 203,
        }

    def _generate_output_signal_map(self):
        return {
            "Wiper_Int_Sts": 211,
            "Wiper_Low_Sts": 212,
            "Wiper_High_Sts": 213,
        }

    def activate_wiper_mode(self, mode_name, duration=10):
        # Ensure valid mode
        if mode_name not in self.input_signal_map:
            raise ValueError(f"Invalid wiper mode: {mode_name}")

        # Define dependencies and exclusivity
        mode_dependencies = {
            "Wiper_Int": [],
            "Wiper_Low": ["Wiper_Int"],
            "Wiper_High": ["Wiper_Int", "Wiper_Low"]
        }

        all_modes = ["Wiper_Int", "Wiper_Low", "Wiper_High"]
        to_activate = mode_dependencies.get(mode_name, []) + [mode_name]
        to_deactivate = list(set(all_modes) - set(to_activate))

        # Activate required modes
        for mode in to_activate:
            signal_id = self.input_signal_map[mode]
            self.send_integer_data(signal_id)
            self.send_integer_data(1)
            print(f"Activated wiper mode: {mode} (ID: {signal_id})")

        end_time = time.time() + duration
        while time.time() < end_time:
            for mode in to_activate:
                signal_id = self.input_signal_map[mode]
                self.send_integer_data(signal_id)
                self.send_integer_data(1)
            time.sleep(1)

        # Deactivate all
        for mode in all_modes:
            signal_id = self.input_signal_map[mode]
            self.send_integer_data(signal_id)
            self.send_integer_data(0)
            print(f"Deactivated wiper mode: {mode} (ID: {signal_id})")


# Example usage
if __name__ == "__main__":
    hil = HILSimulator(com_port="COM13")
    try:
        hil.connect()

        hil.activate_wiper_mode("Wiper_Int", duration=10)
        hil.get_output_signal("Wiper_Int_Sts")

        hil.activate_wiper_mode("Wiper_Low", duration=10)
        hil.get_output_signal("Wiper_Low_Sts")

        hil.activate_wiper_mode("Wiper_High", duration=10)
        hil.get_output_signal("Wiper_High_Sts")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        hil.disconnect()
