int motor_pin_1 = 7;    // Declare variable to store pin value connected to motor driver pin 1
int motor_pin_2 = 6;    // Declare variable to store pin value connected to motor driver pin 2

int push_button = 8;    // Declare variable to store pin value of push button

void setup(){
  Serial.begin(9600);   // set the serial baud rate to 9600
  
  pinMode(motor_pin_1, OUTPUT); // set motor pin 1 as OUTPUT
  pinMode(motor_pin_2, OUTPUT); // set motor pin 2 as OUTPUT

  pinMode(push_button, INPUT);  // set push button to take INPUT
}

void loop(){
  if(digitalRead(push_button)){   // check if button is pressed
    digitalWrite(motor_pin_1, HIGH);    // supply 5V to first motor pin
    digitalWrite(motor_pin_2, LOW);    // supply 0V to second motor pin
    Serial.println("Motor running Clock Wise - Button pressed");
  }else{    // if button is not pressed
    digitalWrite(motor_pin_1, LOW);    // supply 0V to first motor pin
    digitalWrite(motor_pin_2, HIGH);    // supply 5V to second motor pin
    Serial.println("Motor running Anti-ClockWise - Button released");
  }
}

