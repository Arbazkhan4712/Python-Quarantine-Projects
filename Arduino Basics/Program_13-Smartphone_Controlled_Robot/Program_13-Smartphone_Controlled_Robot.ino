#include <SoftwareSerial.h>

SoftwareSerial mySerial(2,3);   // turns digital pin 2 as RX and pin 3 as TX

int left_motor_pin_1 = 7;    // Declare variable to store pin value connected to left motor driver pin 1
int left_motor_pin_2 = 6;    // Declare variable to store pin value connected to left motor driver pin 2

int right_motor_pin_1 = 5;    // Declare variable to store pin value connected to right motor driver pin 1
int right_motor_pin_2 = 4;    // Declare variable to store pin value connected to right motor driver pin 2

void setup() {
  Serial.begin(9600);   // sets the serial baud rate to 9600
  mySerial.begin(38400);   // sets the serial baid rate for android to bluetooth module connection to 38400

  pinMode(left_motor_pin_1, OUTPUT); // set left motor pin 1 as OUTPUT
  pinMode(left_motor_pin_2, OUTPUT); // set left motor pin 2 as OUTPUT

  pinMode(right_motor_pin_1, OUTPUT); // set right motor pin 1 as OUTPUT
  pinMode(right_motor_pin_2, OUTPUT); // set right motor pin 2 as OUTPUT
}

char data;    // character data type used to store data received from Smartphone

void loop() {
  if(mySerial.available()){   // checks if data is being sent via smartphone
    
    data = mySerial.read();   // reads the data from smartphone and stores into 'data' character variable type
    
    if(data == 'F'){    // check if Up arrow has been pressed on Android App
      goFront();    // if yes, move robot in front direction
    }
    else if(data == 'B'){   // check Down Back arrow has been pressed on Android App
      reverse();    // if yes, move robot in reverse direction
    }
    else if(data == 'L'){   // check if Left arrow has been pressed on Android App
      turnLeft();   // if yes, move robot in left direction
    }
    else if(data == 'R'){   // check if Right arrow has been pressed on Android App
      turnRight();    // if yes, move robot in right direction
    }
    else if(data == 'S'){   // check if any of the arrows has been pressed and then released on Android App
      stopRobot();    // if yes, stop the robot
    }
  }
}


void goFront() {  // this function moves robot in front direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2

  Serial.println("Robot moving forward");   // prints 'Robot moving forward' on Serial Monitor
}

void reverse() {  // this function moves robot reverse
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2

  Serial.println("Robot moving backwards");   // prints 'Robot moving backwards' on Serial Monitor
}

void turnLeft() {  // this function turns robot in left direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2

  Serial.println("Robot turning left");   // prints 'Robot turing left' on Serial Monitor
}

void turnRight() {  // this function turns robot in right direction
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2

  Serial.println("Robot turning right");    // prints 'Robot turning right' on Serial Monitor
}

void stopRobot() {  // this function turns robot in right direction
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2

  Serial.println("Robot Stopped");  // prints 'Robot Stopped on Serial Monitor
}
