int led = 11;   // Declare an Integer variable with value 12, 12 defines that we going to use pin 12 on Arduino t blink our LED
int pot_pin = A0;    // Declare a variable for Potentiometer, Potentiometer gives input to Arduino through this pin 

void setup(){   
  Serial.begin(9600);     // sets 9600 as baud rate for serial communication
  pinMode(led, OUTPUT);   // sets the pin 12 as OUTPUT, now the Arduino is ready to supply 5V through this pin
  pinMode(pot_pin, INPUT);  // sets pin A0 as INPUT, now Arduino can read analog value from the Potentiometer
}

int brightness = 0;   // declare a variable to store intensity value of LED

void loop(){  
  brightness = map(analogRead(pot_pin),0,1023,0,255);   // read pot value into our brightness variable
  Serial.println(brightness);   // print value of brightness on Serial Monitor
  analogWrite(led, brightness);  // supplies a PWM signal of the value in brightness
}

