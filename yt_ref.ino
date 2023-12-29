#include <Arduino.h>
#include <Servo.h>
Servo myservo;

int emgPin=A1;
int emgValue=0;
int servoPin=9;

void setup() {
  myservo.attach(servoPin);
  Serial.begin(115200);
  // put your setup code here, to run once:

}

void loop() {
  emgValue=analogRead(emgPin);
  int servoPos=map(emgValue,0,1023,0,360);
  myservo.write(servoPos);
  Serial.println(emgValue);
  delay(10);
  // put your main code here, to run repeatedly:

}
