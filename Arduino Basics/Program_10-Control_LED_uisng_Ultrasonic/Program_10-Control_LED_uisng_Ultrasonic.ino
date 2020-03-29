int trigger_pin = 8;  // Declare variable to store value of pin connected to trigger pin of ultrasonic
int echo_pin = 9;  // Declare variable to store value of pin connected to echo pin of ultrasonic

int green_led = 13;   // Declare variable to store value of pin connected to green led
int red_led = 12;    // Declare variable to store value of pin connected to red led

int distance;   // declare a variable to store distance value
long duration;  // store value returned by pulseIn function

void setup() {
  Serial.begin(9600);   // sets the serial baud rate to 9600
  pinMode(trigger_pin, OUTPUT);   // sets trigger_pin as OUTPUT
  pinMode(echo_pin, INPUT);   // sets echo_pin as INPUT

  pinMode(green_led, OUTPUT); // sets green led pin to OUTPUT
  pinMode(red_led, OUTPUT); // sets red led pin to OUTPUT 
}

void loop() {
  digitalWrite(trigger_pin, LOW);    // apply 0V to trigger pin
  delayMicroseconds(2);   // pause program for 2 micro seconds -> 1 second = 1000000 micro seconds
  digitalWrite(trigger_pin, HIGH);       // apply 5V to trigger pin
  delayMicroseconds(10);    // pause program for 2 micro seconds -> 1 second = 1000000 micro seconds
  digitalWrite(trigger_pin, LOW);        // apply 0V to trigger pin

  duration = pulseIn(echo_pin, HIGH);   // listen for echo
  distance = (duration / 2) / 29.1;   // calculating distance in cm

  Serial.print("Distance : ");    // print distance data on Serial monitor
  Serial.print(distance);
  Serial.print(" cm");

  if(distance < 15){  // checks if distance of Object is less than 15 cm
    digitalWrite(red_led, HIGH);  // turns on red led
    digitalWrite(green_led, LOW);  // turns off green led
    Serial.println("   Danger");   // print "Danger" if object is near
  }else{    // distance less than 15 cm
    digitalWrite(green_led, HIGH);  // turns on green led
    digitalWrite(red_led, LOW);  // turns off red led
    Serial.println("   Safe");   // print "Safe" if object is far
  }
}
