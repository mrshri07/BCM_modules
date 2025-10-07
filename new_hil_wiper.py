import time
import serial


class HILSimulator:
    def __init__(self, com_port, baudrate=115200, timeout=1):
        self.com_port = com_port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self):
        try:
            self.serial_conn = serial.Serial(self.com_port, baudrate=self.baudrate, timeout=self.timeout)
            print(f"Connected to HIL simulator on {self.com_port}")
        except Exception as e:
            raise ConnectionError(f"Connection failed: {e}")

    def disconnect(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            print("Disconnected from HIL simulator")

    def send_integer_data(self, data):
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("No active connection")
        self.serial_conn.write(data.to_bytes(4, byteorder='little', signed=True))
        print(f"Sent integer data: {data}")

    def activate_signal(self, signal_id, duration=1):
        """Activates a signal by sending signal ID and '1', then resets it after `duration` seconds"""
        self.send_integer_data(signal_id)
        self.send_integer_data(1)
        print(f"Activated signal {signal_id}")
        time.sleep(duration)
        self.send_integer_data(signal_id)
        self.send_integer_data(0)
        print(f"Deactivated signal {signal_id}")


# Main execution
if __name__ == "__main__":
    hil = HILSimulator(com_port="COM6")

    try:
        hil.connect()

        # Step 1: Activate signal 201
        hil.activate_signal(201, duration=2)

        # Step 2: Wait then activate 202
        time.sleep(1)
        hil.activate_signal(202, duration=4)

        # Step 3: Wait then activate 203
        time.sleep(1)
        hil.activate_signal(203, duration=6)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        hil.disconnect()
