# pip install opencv-python
# pip install opencv-contrib-python
# pip install pillow

import cv2
import pandas as pd
from PIL import Image, ImageTk

csv_path = 'assets/colors.csv'
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

def from_rgb(rgb):
	"""translates an rgb tuple of int to a tkinter friendly color code
	"""
	r, g, b = rgb
	return f'#{r:02x}{g:02x}{b:02x}'

def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

class ColorDetector:
	def __init__(self, file):
		self.image = cv2.imread(file)
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

	def display_image(self, size):
		self.image = cv2.resize(self.image, size)
		tkimg = Image.fromarray(self.image)
		tkimg = ImageTk.PhotoImage(tkimg)

		return tkimg

	def get_pixel_value(self, pos):
		x, y = pos
		return self.image[y,x]

