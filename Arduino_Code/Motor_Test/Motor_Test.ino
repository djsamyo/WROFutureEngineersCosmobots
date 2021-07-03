#include <Servo.h> 
#include <AFMotor.h>

Servo myservo;  // create servo object to control a servo

int servoId;
String serialData;
String servoPosition;
String motorSpeed;

void dataToString(String data){
  servoPosition = data.substring(0,3);
  motorSpeed = data.substring(4,7);

}

void setup() {
  Serial.begin(9600);
  myservo.attach(11); // attaches the servo on pin 10 to the servo object   
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  if (Serial.available()){
    //Serial code
  
    serialData = Serial.readStringUntil('\n');
    serialData.trim();
    dataToString(serialData);

    //motor code
    myservo.write(servoPosition.toInt());
  }

  //Turn on motor and change speed
  analogWrite(6, motorSpeed.toInt());.
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);

  /*for (int i = 80; i <= 180; i++){
    myservo.write(i);
    delay(10);
  }

  for (int i = 180; i >= 80; i--){
    myservo.write(i);
    delay(10);
  }*/
}
