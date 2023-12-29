#include <Servo.h>

Servo myservo;  // Create a servo object

int inputMin = 0;     // Minimum input value (adjust as needed)
int inputMax = 1023;  // Maximum input value (adjust as needed)
int servoMin = 0;     // Minimum servo angle (adjust as needed)
int servoMax = 180;   // Maximum servo angle (adjust as needed)

void setup() {
  myservo.attach(9);  // Attach the servo to pin 9
  Serial.begin(9600);
}

void loop() {
  int inputValue, servoAngle;

  Serial.println("Enter an input value between 0 and 1023:");
  while (Serial.available() <= 0) {
    // Wait for input
  }
  inputValue = digitalRead(9);  // Read the emg input value

  // Map the input value to the servo angle within the specified range
  servoAngle = map(inputValue, inputMin, inputMax, servoMin, servoMax);

  myservo.write(servoAngle);  // Move the servo to the mapped angle
  Serial.print("Moving servo to ");
  Serial.print(servoAngle);
  Serial.println(" degrees");
  delay(500);  // Delay to prevent rapid movements
}
