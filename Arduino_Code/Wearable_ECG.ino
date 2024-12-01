// Example Arduino ECG data collection
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("ECG Data Collection Started");
}

void loop() {
  // Simulate ECG data (replace with real ECG sensor readings)
  float ecg_signal = random(0, 1023) / 1023.0 * 5.0;
  Serial.println(ecg_signal);
  delay(10);  // Simulate a sampling rate of 100 Hz
}
