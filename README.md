ESP32 Traffic Light Controller
A simple MicroPython-based traffic light controller project. This project demonstrates how to use Object-Oriented Programming (OOP) to control hardware components like LEDs on an ESP32.

Hardware Connections
The code is configured for the following pinout (as seen in my build):

Red LED: Pin 12

Yellow LED: Pin 13

Green LED: Pin 14

Common Ground: GND via 220Ω resistors

Features
Standard Cycle: Implements a full traffic sequence: Red -> Red+Yellow -> Green -> Flashing Green -> Yellow.

Alarm Mode: A simple yellow-blinking emergency mode.

Clean Code: Uses a TrafficLight class for better modularity.

How to Run
Install VS Code with the MicroPico extension.

Connect your ESP32.

Upload the main.py file to your device.

The script will start automatically on boot.
