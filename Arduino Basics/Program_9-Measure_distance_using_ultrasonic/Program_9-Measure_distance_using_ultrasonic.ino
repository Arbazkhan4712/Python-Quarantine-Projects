int trigger_pin = 8;  // Declare variable to store value of pin connected to trigger pin of ultrasonic
int echo_pin = 9;  // Declare variable to store value of pin connected to echo pin of ultrasonic

int distance;   // declare a variable to store distance value
long duration;  // store value returned by pulseIn function

int led = 12;
void setup() {
  Serial.begin(9600);   // sets the serial baud rate to 9600
  pinMode(trigger_pin, OUTPUT);   // sets trigger_pin as OUTPUT
  pinMode(echo_pin, INPUT);   // sets echo_pin as INPUT
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(trigger_pin, LOW);    // apply 0V to trigger pin
  delayMicroseconds(6);   // pause program for 2 micro seconds -> 1 seconds = 1000000 micro seconds
  digitalWrite(trigger_pin, HIGH);       // apply 5V to trigger pin
  delayMicroseconds(12);    // pause program for 2 micro seconds -> 1 seconds = 1000000 micro seconds
  digitalWrite(trigger_pin, LOW);        // apply 0V to trigger pin

  duration = pulseIn(echo_pin, HIGH);   // listen for echo
  distance = (duration / 2) / 29.1;   // calculating distance in cm

  Serial.print("Distance : ");    // print distance data on Serial monitor
  Serial.print(distance);
  Serial.println(" cm");
  if(distance<=50)
  {

    digitalWrite(led, HIGH);
  }
  else
  {
      digitalWrite(led, LOW);
  }
}

