ESP32 Traffic Light Controller

Hardware Connections
The code is configured for the following pinout (as seen in my build):

Red LED: Pin D12

Yellow LED: Pin D13

Green LED: Pin D14

Common Ground: GND via 220Ω-330Ω resistors

Features
Standard Cycle: Implements a full traffic sequence: Red -> Red+Yellow -> Green -> Flashing Green -> Yellow.

Alarm Mode: A simple yellow-blinking emergency mode.


How to Run
Install VS Code with the MicroPico extension.

Connect your ESP32.

Upload the main.py file to your device.

The script will start automatically on boot.


<img width="350" height="550" alt="presentation" src="https://github.com/user-attachments/assets/0e178cda-88fb-426e-9876-46d5cb1d047c" />

