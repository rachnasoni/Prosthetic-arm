const int emgPin = A0;    // Analog pin for EMG sensor
const int outputPin = 9;  // Digital pin for output (e.g., LED)

float alpha = 0.1;         // Filter coefficient (adjust as needed)
float filteredEMG = 0.0;   // Filtered EMG value

void setup() {
  Serial.begin(9600);
  pinMode(outputPin, OUTPUT);
}

void loop() {
  // Read raw EMG value
  int emgValue = analogRead(emgPin);

  // Apply high-pass filter (remove baseline)
  filteredEMG = alpha * (filteredEMG + emgValue - analogRead(emgPin));

  // Adjust the threshold based on your specific setup
  int threshold = 50;

  if (filteredEMG > threshold) {
    // Perform action when muscle activity is detected (e.g., light up LED)
    digitalWrite(outputPin, HIGH);
  } else {
    digitalWrite(outputPin, LOW);
  }

  // Print filtered EMG value to Serial Monitor
  Serial.println("Filtered EMG Value: " + String(filteredEMG));

  delay(50); // Adjust delay as needed for your specific setup
}
