import subprocess
import sys
import os
returned_text = subprocess.check_output("python3 recognition.py", shell=True, universal_newlines=True)
print("Attendence Marked")
print(returned_text)
remember = open('text.txt','w')
remember.write(returned_text)
remember.close()
