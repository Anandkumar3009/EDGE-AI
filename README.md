# EDGE-AI: TinyML Activity Detection with Nicla Vision

This repository contains the complete workflow for the "Day 1 - TinyML" project, focusing on hardware setup, real-time data collection, and IMU sensor integration using the **Arduino Nicla Vision**.

## 📂 Repository Structure
* [cite_start]**`data/`**: Scripts for wireless data transmission (`main.py`) and host-side collection. [cite: 134]
* [cite_start]**`docs/`**: Official datasheets and step-by-step setup guides. [cite: 1]
* **`examples/`**: Basic hardware tests including LED blinking, camera initialization, and IMU thresholding.
* [cite_start]**`results/`**: Visual outputs and logs from the data collection experiments. [cite: 387]

---

## 🛠️ Hardware Setup & Data Collection

To collect high-quality IMU data for activity recognition, follow these steps:

### 1. Network Configuration
* [cite_start]**Hotspot**: Turn on your mobile hotspot and connect your PC to it. [cite: 2, 3]
* [cite_start]**IP Identification**: Open your command prompt, run `ipconfig`, and record the IPv4 address of your PC (e.g., `192.168.67.111`). [cite: 10, 33]
* [cite_start]**Firmware Sync**: Update `main.py` with your mobile hotspot SSID/Key and the PC's IP address. [cite: 75]

### 2. Device Deployment
* [cite_start]Connect the Nicla Vision to your PC via USB and open the OpenMV IDE. [cite: 36, 37]
* [cite_start]Upload and run `main.py`. [cite: 76]
* [cite_start]**Green Light**: Once the board successfully connects to Wi-Fi, it will light up a green light. [cite: 77]
* [cite_start]You may then disconnect the board from the PC and power it via a portable power bank. [cite: 80, 81]

### 3. Data Acquisition
* [cite_start]Run `receive_data.py` in VS Code on your PC. [cite: 82, 136]
* [cite_start]Enter the activity label when prompted (e.g., `sit`, `walk`, `swing`). [cite: 137, 181]
* [cite_start]**Duration**: Perform the activity for at least **2 minutes** to ensure data integrity. [cite: 299]
* [cite_start]The script will automatically terminate and save a timestamped CSV to the `imu_data/` folder. [cite: 300, 387]

---

## 🛰️ Sensor Specifications (IMU)
The project utilizes the onboard **LSM6DSOX** 6-axis IMU. Data is captured in the following format:
* **Accelerometer**: $A_x, A_y, A_z$ (G-Force)
* **Gyroscope**: $G_x, G_y, G_z$ (Degrees/sec)
* [cite_start]**Timestamp**: Milliseconds since device boot [cite: 120]
