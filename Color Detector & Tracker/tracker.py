# pip install opencv-python
# pip install opencv-contrib-python
# pip install pillow

import cv2
import requests
import numpy as np
from PIL import Image, ImageTk

class ImageColorTracker:
	def __init__(self, file):
		self.image_orig = cv2.imread(file)
		self.image = cv2.cvtColor(self.image_orig, cv2.COLOR_BGR2RGB)

		self.img = cv2.resize(self.image, (450,400))
		self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

	def display_original_image(self, size):
		tkimg = cv2.resize(self.image, size)
		tkimg = Image.fromarray(tkimg)
		tkimg = ImageTk.PhotoImage(tkimg)

		return tkimg

	def detect_from_image(self, arr1, arr2):
		lower = np.array(arr1)
		upper = np.array(arr2)
		mask = cv2.inRange(self.hsv, lower, upper)

		detected = cv2.bitwise_and(self.img, self.img, mask=mask)
		tkimg = Image.fromarray(detected)
		tkimg = ImageTk.PhotoImage(tkimg)

		return tkimg

class RealtimeColorTracker:
	def __init__(self, src):
		self.src = src

	def get_from_camera(self, arr1, arr2):
		try:
			print(arr1, arr2)
			cap = cv2.VideoCapture(self.src)
			if not cap.isOpened():
				return "Cannot open camera"
			ret, frame = cap.read()
			if ret:
				original, detected = self.detect_color(frame, arr1, arr2)
				return original, detected
		except:
			return "Cannot open camera"
		
	def get_from_stream(self, arr1, arr2):
		try:
			r = requests.get(self.src)
			img_arr = np.array(bytearray(r.content), dtype=np.uint8)
			img = cv2.imdecode(img_arr, -1)
			original, detected = self.detect_color(img, arr1, arr2)
			return original, detected
		except:
			return "Cannot connect to stream"

	def detect_color(self, img, arr1, arr2):
		orig = cv2.resize(img, (250,200))
		orig = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

		img = cv2.resize(img, (450,400))
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		

		lower = np.array(arr1)
		upper = np.array(arr2)
		mask = cv2.inRange(hsv, lower, upper)

		detected = cv2.bitwise_and(img, img, mask=mask)
		detected = Image.fromarray(detected)
		detected = ImageTk.PhotoImage(detected)

		original =  Image.fromarray(orig)
		original = ImageTk.PhotoImage(original)

		return original, detected