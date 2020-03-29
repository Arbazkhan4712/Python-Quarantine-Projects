int led = 12;   // Declare an Integer variable with value 12, 12 defines that we going to use pin 12 on Arduino t blink our LED

// this function runs only once
void setup(){   
  pinMode(led, OUTPUT);   // sets the pin 12 as OUTPUT, now the Arduino is ready to supply 5V through this pin
}

// this function runs infinitely
void loop(){
  digitalWrite(led, HIGH);  // supplies 5V through pin 12, LED on
  delay(1000);    // pause the program for 1000 ms i.e 1 second
  digitalWrite(led, LOW);   // sets the LED off
  delay(1000);  // pause program for 1 second
}

