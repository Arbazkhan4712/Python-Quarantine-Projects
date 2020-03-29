int led = 11;   // Declare an Integer variable with value 12, 12 defines that we going to use pin 12 on Arduino t blink our LED
int pot_pin = A0;    // Declare a variable for potentiometer pin value
int push_button = 7;    // Declare a variable for push button pin value

void setup() {
  Serial.begin(9600);     // sets 9600 as baud rate for serial communication
  pinMode(led, OUTPUT);   // sets the pin 12 as OUTPUT, now the Arduino is ready to supply 5V through this pin
  pinMode(pot_pin, INPUT);  // sets pin A0 as INPUT pin, now Arduino can read input from our Potentiometer
  pinMode(push_button, INPUT);   // sets pin 7 as INPUT pin, now Arduino can read input from Push button
}

int pot_value = 0;

void loop() {
  pot_value = map(analogRead(pot_pin),0,1023,0,254);    // read and map pot value and store in variable
  
  if (pot_value > 155 && digitalRead(push_button)) {  // check if Pot has been rotated more than half and push button is also pressed
    analogWrite(led, pot_value);    // turns LED ON eith given intensity value
    Serial.println("LED is ON");   // print that led is ON on Serial Monitor
  } else {    // either push button is not pressed or pot value is less
    digitalWrite(led, LOW);    // turns LED OFF
    Serial.println("LED is OFF");   // print that led is OFF on Serial Monitor
  }
}

