<p align="center">
  <h1>🚦 ESP32 Traffic Light Controller</h1>
</p>

<p align="center">
  <img width="350" alt="presentation" src="https://github.com/user-attachments/assets/0e178cda-88fb-426e-9876-46d5cb1d047c" />
</p>

---

### 🔌 Hardware Connections
<p align="left">
The code is configured for the following pinout (as seen in my build):

*   🔴 **Red LED**: Pin `D12` via 220Ω-330Ω resistors
*   🟡 **Yellow LED**: Pin `D13` via 220Ω-330Ω resistors
*   🟢 **Green LED**: Pin `D14` via 220Ω-330Ω resistors
*   🔌 **Common Ground**: `GND`
</p>

---

### ✨ Features
*   🔄 **Normal Cycle**: Implements a full traffic sequence: **Red** -> **Red+Yellow** -> **Green** -> **Flashing Green** -> **Yellow**.
*   ⚠️ **Alarm Mode**: A simple yellow-blinking emergency mode.

---

### 🚀 How to Run
1.  💻 **Install**: VS Code with the MicroPico extension.
2.  🔌 **Connect**: Plug in your ESP32 via USB.
3.  📤 **Upload**: Transfer the `main.py` file to your device.
4.  ⚙️ **Boot**: The script will start automatically on boot.

---

<p align="center">
  by Nick 🛠️
</p>
