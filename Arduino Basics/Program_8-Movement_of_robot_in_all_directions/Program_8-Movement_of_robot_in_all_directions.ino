int left_motor_pin_1 = 7;    // Declare variable to store pin value connected to left motor driver pin 1
int left_motor_pin_2 = 6;    // Declare variable to store pin value connected to left motor driver pin 2

int right_motor_pin_1 = 5;    // Declare variable to store pin value connected to right motor driver pin 1
int right_motor_pin_2 = 4;    // Declare variable to store pin value connected to right motor driver pin 2

void setup() {
  Serial.begin(9600);   // set the serial baud rate to 9600

  pinMode(left_motor_pin_1, OUTPUT); // set left motor pin 1 as OUTPUT
  pinMode(left_motor_pin_2, OUTPUT); // set left motor pin 2 as OUTPUT

  pinMode(right_motor_pin_1, OUTPUT); // set right motor pin 1 as OUTPUT
  pinMode(right_motor_pin_2, OUTPUT); // set right motor pin 2 as OUTPUT
}

void loop() {
  goFront();  // robot moves in front direction
  delay(3000);    // pause the program for 3 seconds

  reverse();  // robot moves reverse
  delay(3000);    // pause the program for 3 seconds

  turnLeft();  // turns robot in left direction
  delay(3000);    // pause the program for 3 seconds

  turnRight();  // turns robot in right direction
  delay(3000);    // pause the program for 3 seconds
}

void goFront() {  // this function moves robot in front direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2

  Serial.println("Robot moving in Front Direction");
}

void reverse() {  // this function moves robot reverse
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2

  Serial.println("Robot moving in Backward Direction");
}

void turnRight() {  // this function turns robot in left direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2

  Serial.println("Robot turning in Right Direction");
}

void turnLeft() {  // this function turns robot in right direction
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2

  Serial.println("Robot in Left Direction");
}
