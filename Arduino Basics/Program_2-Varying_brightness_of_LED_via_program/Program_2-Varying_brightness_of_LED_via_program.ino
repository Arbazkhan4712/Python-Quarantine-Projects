int led = 11;   // Declare an Integer variable with value 12, 12 defines that we going to use pin 12 on Arduino t blink our LED

void setup(){   
  Serial.begin(9600);     // sets 9600 as baud rate for serial communication
  pinMode(led, OUTPUT);   // sets the pin 12 as OUTPUT, now the Arduino is ready to supply 5V through this pin
}

int brightness = 0;   // declare a variable to store intensity value of LED

void loop(){  
  brightness = brightness + 1;  // increment value of brightness by 1
  Serial.println(brightness);   // print value of brightness on Serial Monitor
  analogWrite(led, brightness);  // supplies a PWM signal of the value in brightness
  delay(50);    // pause the program for 10 ms

  if(brightness > 255){   // if value of brightness greater than 255, set it to 0
    brightness = 0;   // brightness set to 0
  }
}

