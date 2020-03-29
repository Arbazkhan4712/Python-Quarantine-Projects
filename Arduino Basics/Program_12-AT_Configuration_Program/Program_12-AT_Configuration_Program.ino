/*
 The Arduino hardware has built-in support for serial
 communication on pins 0 and 1 (which also goes to the 
 computer via the USB connection). The native serial 
 support happens via a piece of hardware (built into 
 the chip) called a UART. This hardware allows the 
 Atmega chip to receive serial communication even 
 while working on other tasks, as long as there room
 in the 64 byte serial buffer.
 
 The SoftwareSerial library has been developed to allow
 serial communication on other digital pins of the Arduino,
 using software to replicate the functionality (hence the
 name "SoftwareSerial"). It is possible to have multiple 
 software serial ports with speeds up to 115200 bps.
 A parameter enables inverted signaling for devices 
 which require that protocol.
 */
 
#include <SoftwareSerial.h>
SoftwareSerial mySerial(2,3);

void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
  mySerial.begin(38400);
}

void loop() {
  // read from port 1, send to port 0:
  if (mySerial.available()) {
    int inByte = mySerial.read();
    Serial.write(inByte);
  }

  // read from port 0, send to port 1:
  if (Serial.available()) {
    int inByte = Serial.read();
    mySerial.write(inByte);
  }
}
