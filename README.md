# Wearable ECG Anomaly Detection

This project demonstrates how to process wearable ECG data to detect anomalies using Python and Arduino.

## Features
- Real-time ECG data collection using Arduino
- Anomaly detection with Python and Isolation Forest
- Visualization of detected anomalies in ECG signals

## Hardware Requirements
- Arduino-compatible board (e.g., Arduino Nano)
- ECG sensor module
- USB Cable
- PC with Python and VS Code

## Software Requirements
- Arduino IDE
- Python 3.7 or higher
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `pyserial`

## Setup Instructions

### Arduino Setup
1. Upload the `Wearable_ECG.ino` sketch to the Arduino.
2. Connect the Arduino to your PC.

### Python Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/faheem09/Wearable-ECG-Anomaly-Detection.git
   cd Wearable-ECG-Anomaly-Detection
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scriptsctivate
   pip install -r requirements.txt
   ```
3. Run the `data_collection.py` script to collect ECG data:
   ```bash
   python Python_Code/data_collection.py
   ```
4. Run the `anomaly_detection.py` script to detect anomalies:
   ```bash
   python Python_Code/anomaly_detection.py
   ```

## Example Visualization
![ECG Anomaly Detection Plot](example_plot.png)

## License
This project is licensed under the MIT License.
