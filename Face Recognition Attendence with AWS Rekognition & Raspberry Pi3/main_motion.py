import subprocess
import sys
import os
from gpiozero import MotionSensor
from signal import pause
pir = MotionSensor(4)# Connect Motion sensor with GPIO 4
def face():
	returned_text = subprocess.check_output("python3 match.py", shell=True, universal_newlines=True)
	print("Result")
	print(returned_text)
	remember = open('text.txt','w')
	remember.write(returned_text)
	remember.close()


while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    face()
    print ("done!")
    exit()
