# EDGE-AI Project Repository

* **[Day 1: TinyML & Data Collection](./Day_01_TinyML/README.md)** - Hardware setup with Nicla Vision and IMU data acquisition.

Here is the complete workflow for the "Day 1 - TinyML" project, focusing on hardware setup, real-time data collection, and IMU sensor integration using the **Arduino Nicla Vision**.

## 📂 Repository Structure
* **data/**: Scripts for wireless data transmission (`main.py`) and host-side collection.
* **docs/**: Official datasheets and step-by-step setup guides.
* **examples/**: Basic hardware tests including LED blinking, camera initialization, and IMU thresholding.
* **results/**: Visual outputs and logs from the data collection experiments.

---

## 🛠️ Hardware Setup & Data Collection

To collect high-quality IMU data for activity recognition, follow these steps:

### 1. Network Configuration
* **Hotspot**: Turn on your mobile hotspot and connect your PC to it.
* **IP Identification**: Open your command prompt, run `ipconfig`, and record the IPv4 address of your PC (e.g., `192.168.67.111`).
* **Firmware Sync**: Update `main.py` with your mobile hotspot SSID/Key and the PC's IP address.

### 2. Device Deployment
* **Connect**: Connect the Nicla Vision to your PC via USB and open the OpenMV IDE.
* **Upload**: Upload and run `main.py`.
* **Green Light**: Once the board successfully connects to Wi-Fi, it will light up a green light.
* **Power**: You may then disconnect the board from the PC and power it via a portable power bank.

### 3. Data Acquisition
* **Run**: Run `receive_data.py` in VS Code on your PC.
* **Label**: Enter the activity label when prompted (e.g., `sit`, `walk`, `swing`).
* **Duration**: Perform the activity for at least **2 minutes** to ensure data integrity.
* **Auto-save**: The script will automatically terminate and save a timestamped CSV to the `imu_data/` folder.
