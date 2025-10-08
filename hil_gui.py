import tkinter as tk
from tkinter import ttk, messagebox
import serial.tools.list_ports
from HILSimulator import HILSimulator  # assuming your simulator code is in a file named HILSimulator.py
import time
import threading

class HILSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HIL Wiper Control")
        self.simulator = None

        self.create_widgets()

    def create_widgets(self):
        # COM Port Dropdown
        ttk.Label(self.root, text="Select COM Port:").grid(row=0, column=0, padx=10, pady=10)
        self.combobox = ttk.Combobox(self.root, values=self.get_serial_ports(), width=15)
        self.combobox.grid(row=0, column=1)

        # Connect Button
        self.connect_btn = ttk.Button(self.root, text="Connect", command=self.connect_simulator)
        self.connect_btn.grid(row=0, column=2, padx=10)

        # Wiper Speed Control
        ttk.Label(self.root, text="Wiper Speed:").grid(row=1, column=0, padx=10)
        self.speed_var = tk.IntVar()
        self.speed_dropdown = ttk.Combobox(self.root, textvariable=self.speed_var,
                                           values=["0-Off", "1-Low", "2-High", "3-Intermittent"], state="readonly")
        self.speed_dropdown.grid(row=1, column=1)
        self.set_speed_btn = ttk.Button(self.root, text="Set Speed", command=self.set_speed)
        self.set_speed_btn.grid(row=1, column=2)

        # Wash Button
        self.wash_btn = ttk.Button(self.root, text="Activate Wash", command=self.activate_wash)
        self.wash_btn.grid(row=2, column=0, columnspan=3, pady=10)

        # Wiper Status
        self.status_btn = ttk.Button(self.root, text="Get Wiper Status", command=self.get_status)
        self.status_btn.grid(row=3, column=0, columnspan=3, pady=5)

        self.status_label = ttk.Label(self.root, text="Status: N/A", foreground="blue")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)

    def get_serial_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect_simulator(self):
        port = self.combobox.get()
        if not port:
            messagebox.showerror("Error", "Please select a COM port.")
            return
        try:
            self.simulator = HILSimulator(port)
            self.simulator.connect()
            messagebox.showinfo("Success", f"Connected to {port}")
        except Exception as e:
            messagebox.showerror("Connection Failed", str(e))

    def set_speed(self):
        if not self.simulator:
            messagebox.showerror("Error", "Not connected to simulator.")
            return
        try:
            speed = int(self.speed_dropdown.get().split('-')[0])
            self.simulator.set_wiper_speed(speed)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def activate_wash(self):
        if not self.simulator:
            messagebox.showerror("Error", "Not connected to simulator.")
            return
        threading.Thread(target=self.simulator.activate_wash, args=(1.5,), daemon=True).start()

    def get_status(self):
        if not self.simulator:
            messagebox.showerror("Error", "Not connected to simulator.")
            return
        try:
            status = self.simulator.get_wiper_status()
            self.status_label.config(text=f"Status: {status}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = HILSimulatorGUI(root)
    root.mainloop()
