// connect four LED's from pin 10 to pin 13

void setup() {
  Serial.begin(9600);     // sets 9600 as baud rate for serial communication
  for (int i = 10; i < 14; i++) { // sets pin 10 to 13 for OUTPUT
    pinMode(i, OUTPUT);
  }
}

void loop() {
  light();  // call for 'light' function
  digitalWrite(10, HIGH);    // turns LED  at pin 10 ON
  digitalWrite(11, HIGH);    // turns LED at pin 11 ON
  digitalWrite(12, HIGH);    // turns LED at pin 12 ON
  digitalWrite(13, HIGH);    // turns LED at pin 13 ON
  delay(1000);  // pause for 1 second
}

void light() {
  for (int i = 10; i < 14; i++) { // loop from value 10 to 13
    if (i == 10) {
      digitalWrite(10, HIGH);    // turns LED  at pin 10 ON
      digitalWrite(11, LOW);    // turns LED at pin 11 OFF
      digitalWrite(12, LOW);    // turns LED at pin 12 OFF
      digitalWrite(13, LOW);    // turns LED at pin 13 OFF
    } else if (i == 11) {
      digitalWrite(10, LOW);    // turns LED  at pin 10 OFF
      digitalWrite(11, HIGH);    // turns LED at pin 11 ON
      digitalWrite(12, LOW);    // turns LED at pin 12 OFF
      digitalWrite(13, LOW);    // turns LED at pin 13 OFF
    } else if (i == 12) {
      digitalWrite(10, LOW);    // turns LED  at pin 10 OFF
      digitalWrite(11, LOW);    // turns LED at pin 11 OFF
      digitalWrite(12, HIGH);    // turns LED at pin 12 ON
      digitalWrite(13, LOW);    // turns LED at pin 13 OFF
    } else {
      digitalWrite(10, LOW);    // turns LED  at pin 10 OFF
      digitalWrite(11, LOW);    // turns LED at pin 11 OFF
      digitalWrite(12, LOW);    // turns LED at pin 12 OFF
      digitalWrite(13, HIGH);    // turns LED at pin 13 ON
    }
    delay(1000);  // pause program for 1 second
  }
}

