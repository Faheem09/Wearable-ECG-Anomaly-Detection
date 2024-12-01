import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load ECG Data
data = pd.read_csv("ecg_data.csv")

# Convert signal to numeric
data['ecg_signal'] = pd.to_numeric(data['ecg_signal'], errors='coerce')
data = data.dropna()

# Train Unsupervised Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

# Detect Anomalies
data["anomaly"] = model.predict(data)
data["anomaly"] = data["anomaly"].apply(lambda x: 1 if x == -1 else 0)

# Visualize ECG Signal with Anomalies
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["ecg_signal"], label="ECG Signal")
plt.scatter(data.index[data["anomaly"] == 1], 
            data["ecg_signal"][data["anomaly"] == 1], color="red", label="Anomalies")
plt.legend()
plt.title("ECG Signal with Detected Anomalies")
plt.show()
