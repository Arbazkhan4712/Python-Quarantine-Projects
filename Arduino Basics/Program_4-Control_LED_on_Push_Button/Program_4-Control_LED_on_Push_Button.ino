int led = 11;   // Declare an Integer variable with value 12, 12 defines that we going to use pin 12 on Arduino t blink our LED
int push_button = 7;    // Declare a variable for push button pin value, push button will be used to turn LED on or off

void setup() {
  Serial.begin(9600);     // sets 9600 as baud rate for serial communication
  pinMode(led, OUTPUT);   // sets the pin 12 as OUTPUT, now the Arduino is ready to supply 5V through this pin
  pinMode(push_button, INPUT);   // sets pin 7 as INPUT pin, now Arduino can read input from Push button
}

void loop() {
  if (digitalRead(push_button)) {  // check if push button is pressed
    digitalWrite(led, HIGH);    // turns LED ON
    Serial.println("LED is ON");   // print that led is ON on Serial Monitor
  } else {    // push button is not pressed
    digitalWrite(led, LOW);    // turns LED OFF
    Serial.println("LED is OFF");   // print that led is OFF on Serial Monitor
  }
}

