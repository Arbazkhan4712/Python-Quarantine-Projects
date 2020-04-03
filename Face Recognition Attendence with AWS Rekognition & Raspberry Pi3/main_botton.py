import subprocess
import sys
import os
from gpiozero import Button
def face():
	returned_text = subprocess.check_output("python3 match.py", shell=True, universal_newlines=True)
	print("Result")
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
