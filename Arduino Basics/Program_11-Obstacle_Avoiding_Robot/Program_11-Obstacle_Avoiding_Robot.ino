int left_motor_pin_1 = 7;    // Declare variable to store pin value connected to left motor driver pin 1
int left_motor_pin_2 = 6;    // Declare variable to store pin value connected to left motor driver pin 2

int right_motor_pin_1 = 5;    // Declare variable to store pin value connected to right motor driver pin 1
int right_motor_pin_2 = 4;    // Declare variable to store pin value connected to right motor driver pin 2

int trigger_pin = 8;  // Declare variable to store value of pin connected to trigger pin of ultrasonic
int echo_pin = 9;  // Declare variable to store value of pin connected to echo pin of ultrasonic

int green_led = 13;   // Declare variable to store value of pin connected to green led
int red_led = 12;    // Declare variable to store value of pin connected to red led

int distance;   // declare a variable to store distance value
long duration;  // store value returned by pulseIn function

void setup() {
  Serial.begin(9600);   // sets the serial baud rate to 9600

  pinMode(left_motor_pin_1, OUTPUT); // set left motor pin 1 as OUTPUT
  pinMode(left_motor_pin_2, OUTPUT); // set left motor pin 2 as OUTPUT

  pinMode(right_motor_pin_1, OUTPUT); // set right motor pin 1 as OUTPUT
  pinMode(right_motor_pin_2, OUTPUT); // set right motor pin 2 as OUTPUT

  pinMode(trigger_pin, OUTPUT);   // sets trigger_pin as OUTPUT
  pinMode(echo_pin, INPUT);   // sets echo_pin as INPUT

  pinMode(green_led, OUTPUT); // sets green led pin to OUTPUT
  pinMode(red_led, OUTPUT); // sets red led pin to OUTPUT
}

void loop() {
  digitalWrite(trigger_pin, LOW);    // apply 0V to trigger pin
  delayMicroseconds(2);   // pause program for 2 micro seconds -> 1 seconds = 1000000 micro seconds
  digitalWrite(trigger_pin, HIGH);       // apply 5V to trigger pin
  delayMicroseconds(10);    // pause program for 2 micro seconds -> 1 seconds = 1000000 micro seconds
  digitalWrite(trigger_pin, LOW);        // apply 0V to trigger pin

  duration = pulseIn(echo_pin, HIGH);   // listen for echo
  distance = (duration / 2) / 29.1;   // calculating distance in cm

  Serial.print("Distance : ");    // print distance data on Serial monitor
  Serial.print(distance);
  Serial.print(" cm ");

  if (distance < 15) { // checks if distance of Object is less than 15 cm
    digitalWrite(red_led, HIGH);  // turns on red led
    digitalWrite(green_led, LOW);  // turns off green led
    Serial.print(" Danger - ");   // print "Danger" if object is near

    turnLeft();  // turns robot in left direction
    Serial.println("Turning Left to Avoid Obstacle");
  } else {   // distance less than 15 cm
    digitalWrite(green_led, HIGH);  // turns on green led
    digitalWrite(red_led, LOW);  // turns off red led
    Serial.print(" Safe - ");   // print "Safe" if object is far
   
    goFront();  // robot moves in front direction
    Serial.println("Going Front");
  }
}


void goFront() {  // this function moves robot in front direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2
}

void reverse() {  // this function moves robot reverse
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2
}

void turnLeft() {  // this function turns robot in left direction
  digitalWrite(right_motor_pin_1, HIGH);   // supplies 5V to right motor pin 1
  digitalWrite(right_motor_pin_2, LOW);   // supplies 0V to right motor pin 2

  digitalWrite(left_motor_pin_1, LOW);   // supplies 0V to left motor pin 1
  digitalWrite(left_motor_pin_2, HIGH);   // supplies 5V to left motor pin 2
}

void turnRight() {  // this function turns robot in right direction
  digitalWrite(right_motor_pin_1, LOW);   // supplies 0V to right motor pin 1
  digitalWrite(right_motor_pin_2, HIGH);   // supplies 5V to right motor pin 2

  digitalWrite(left_motor_pin_1, HIGH);   // supplies 5V to left motor pin 1
  digitalWrite(left_motor_pin_2, LOW);   // supplies 0V to left motor pin 2
}
