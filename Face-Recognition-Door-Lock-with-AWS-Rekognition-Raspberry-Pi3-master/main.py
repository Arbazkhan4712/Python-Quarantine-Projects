import subprocess
import sys
import os
from gpiozero import Button
from gpiozero import LED
from time import sleep
LOCK = LED(17)
def face():
	returned_text = subprocess.check_output("python3 match.py", shell=True, universal_newlines=True)
	a = returned_text
	print("Face Recognized")
	if "---" in a:# Add the name of the person to be recognized from the S3 bucket folder name
		LOCK.on()# Connect Door Lock Digital pin to GPIO 17
		sleep(10)
		LOCK.off()
		print("Door is Open")
	else:
		print("Unknown Person")
	print(returned_text)
	remember = open('text.txt','w')
	remember.write(returned_text)
	remember.close()

button = Button("GPIO26")# Connect the Botton with GPIO 26
while True:
    if button.is_pressed:
        print("Button is pressed")
	face()
        exit()
