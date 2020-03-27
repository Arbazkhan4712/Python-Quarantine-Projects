import pytesseract #pip install tesseract
import os
from PIL import Image
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\tesseract.exe" #Path to the tesseract 

img = Image.open('img2.jpg')# add Image name here with file extention
text = pytesseract.image_to_string(img)
print(text)
remember = open('remember.txt','w')
remember.write(text)
remember.close()
speak(text)