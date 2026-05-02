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

DEMO
<video src="https://github.com/zadvinick/esp32-traffic-light/raw/main/presentation.mp4" width="400" controls>
  Your browser does not support the video tag.
</video>
