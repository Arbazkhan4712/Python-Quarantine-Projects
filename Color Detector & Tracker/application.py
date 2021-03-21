import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from functools import partial

from detector import from_rgb, ColorDetector, get_color_name
from tracker import ImageColorTracker, RealtimeColorTracker

cwd = os.getcwd()

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.features = ['Detect Color', 'Track objects from Image', 'Track objects in Realtime']
		self.current_feature = None
		self.btn_list = []
		self.render_id = None
		self.camera_id = tk.IntVar()
		self.camera_id.set(0)
		self.server_id = tk.StringVar()
		self.connection_option = tk.IntVar()
		self.path = None

		self.draw_frames()
		self.draw_buttons()

	def draw_frames(self):
		self.topbar = tk.Frame(self, width=700, height=49, bg='#363636')
		self.imgFrame = tk.Frame(self, width=450, height=400, bg='white')
		self.rightbar = tk.Frame(self, width=250, height=200, bg='white')
		self.bottomBox = tk.Frame(self, width=250, height=200, bg='dodgerblue3') 

		self.topbar.grid(row=0, column=0, columnspan=2)
		self.imgFrame.grid(row=1, column=0, rowspan=2)
		self.rightbar.grid(row=1, column=1)
		self.bottomBox.grid(row=2, column=1)

		self.topbar.grid_propagate(False)
		self.imgFrame.grid_propagate(False)
		self.rightbar.grid_propagate(False)
		self.bottomBox.grid_propagate(False)

	def draw_buttons(self):
		cindex = 0
		for text in self.features:
			btn = tk.Button(self.topbar, text=text, width=20,
					relief=tk.RAISED, bg='dodgerblue3', fg='white')
			btn.config(command=partial(self.set_selection, btn, text))
			btn.grid(row=0, column=cindex, padx=(60,0), pady=10)
			self.btn_list.append(btn)
			cindex += 1

		self.set_selection(self.btn_list[0], self.features[0])

	def set_selection(self, widget, text):
		if self.render_id:
			self.imgFrame.after_cancel(self.render_id)
			self.render_id = None

		for w in self.imgFrame.winfo_children():
			w.destroy()

		self.canvas = tk.Canvas(self.imgFrame, width =450, height = 400, bg='#afeeee')
		self.canvas.grid(row=0, column=0)
		self.canvas.bind('<Button-1>', self.get_coord)

		for w in self.topbar.winfo_children():
			w.config(relief=tk.FLAT, bg='dodgerblue3')

		for w in self.bottomBox.winfo_children():
			w.destroy()

		for w in self.rightbar.winfo_children():
			w.destroy()

		widget.config(relief=tk.RAISED, bg='green')
		self.canvas.delete('all')
		
		if text == self.features[0]:
			self.bottomBox['bg'] = 'dodgerblue3'
			self.selection_frame(text)
			self.color_label = tk.Label(self.bottomBox, bg='dodgerblue3', fg='white', text='',
							font=('verdana 14'), width=20)
			self.color_label.grid(row=0, column=0, pady=80, padx=1)

		elif text == self.features[1]:
			self.selection_frame(text)

		elif text == self.features[2]:
			self.selection_frame(text)

		self.current_feature = text
		if self.path:
			self.connection_option.set(0)
			self.path = None


	def selection_frame(self, feature):
		if feature == self.features[0]:
			select_btn = tk.Button(self.rightbar, text='Select File', width=10,
						relief=tk.RAISED, bg='dodgerblue3', fg='white',
						command=self.select_file)
			select_btn.grid(row=0, column=0, padx=80, pady=50)

		elif feature == self.features[1]:
			select_btn = tk.Button(self.rightbar, text='Select File', width=10,
						relief=tk.RAISED, bg='dodgerblue3', fg='white',
						command=self.select_file)
			select_btn.grid(row=0, column=0, padx=80, pady=(50,10))

			self.track_btn = tk.Button(self.rightbar, text='Track Color', width=10,
						relief=tk.RAISED, bg='dodgerblue3', fg='white',
						command=self.start_tracking, state=tk.DISABLED)
			self.track_btn.grid(row=1, column=0, padx=80, pady=20)

		elif feature == self.features[2]:
			self.camera_label = ttk.Label(self.rightbar, text='Set PC Camera (default 0)', width=25)
			self.camera_entry = ttk.Entry(self.rightbar, textvariable=self.camera_id, width=22)

			self.server_label = ttk.Label(self.rightbar, text='Enter Server IP', width=25)
			self.server_entry = ttk.Entry(self.rightbar, textvariable=self.server_id, width=22)

			options = {'Use PC Camera':1, 'Connect with Andriod':2}
			r = 0
			for text, value in options.items():
				ttk.Radiobutton(self.rightbar, text=text, variable=self.connection_option,
						value=value, command=self.show_option, width=25).grid(row=r, column=0, padx=10, pady=2)
				r += 1


	def select_file(self):
		self.filepath = filedialog.askopenfilename(initialdir = cwd)
		if self.filepath:
			if self.current_feature == self.features[0]:
				self.CDObj = ColorDetector(self.filepath)
				self.image = self.CDObj.display_image((450, 400))
				self.canvas.create_image(0,0,  anchor=tk.NW, image=self.image)    
				self.canvas.image = self.image 
				self.update()

			elif self.current_feature == self.features[1]:
				for w in self.bottomBox.winfo_children():
					w.destroy()
				self.TDObj = ImageColorTracker(self.filepath)
				self.image = self.TDObj.display_original_image((250, 200))
				self.imglabel = tk.Label(self.bottomBox, image=self.image)
				self.imglabel.grid(row=0, column=0)

				self.im = self.TDObj.display_original_image((450, 400))
				self.canvas.destroy()
				self.tracked_img = tk.Label(self.imgFrame, image=self.im)
				self.tracked_img.grid(row=0, column=0)
				self.update()
				self.track_btn.config(state=tk.NORMAL)

	def get_coord(self, event):
		x, y = event.x, event.y

		if self.current_feature == self.features[0]:
			color = self.CDObj.get_pixel_value((x,y))
			hex_color = from_rgb(list(color))
			self.bottomBox['bg'] = hex_color
			self.update()
			cname = get_color_name(*color)
			if sum(color) >= 600:
				fg = 'white'
			else:
				fg = 'black'
			self.color_label.config(fg=fg, text=cname)

	def create_trackbar(self):
		self.lh_value = tk.IntVar()
		self.ls_value = tk.IntVar()
		self.lv_value = tk.IntVar()
		self.hh_value = tk.IntVar()
		self.hs_value = tk.IntVar()
		self.hv_value = tk.IntVar()

		self.hh_value.set(255)
		self.hs_value.set(255)
		self.hv_value.set(255)

		self.slider_arr = [self.lh_value, self.ls_value, self.lv_value,
					  self.hh_value, self.hs_value, self.hv_value]

		for index, variable in enumerate(self.slider_arr):
			if  index <= 2:
				from_, to, c = 0, 255, 0
				r = (2 * index) + 1
			else:
				from_, to, c = 0, 255, 1
				r = (2 * (index - 3)) + 1

			slider = ttk.Scale(self.rightbar, from_ = from_, to = to, orient = tk.HORIZONTAL)
			slider['variable'] = variable
			slider['command'] = self.print_val
			slider.grid(row=r, column=c, padx=(12,5), pady=(2,15))

		for index, text in enumerate(['Hue (low/high)', 'Saturation (low/high)', 'Value (low/high)']):
			lbl = tk.Label(self.rightbar, text=text, width=30, anchor='w')
			lbl.grid(row=2*index, column=0, columnspan=2)

		if self.current_feature == self.features[1]:
			self.render_id = self.imgFrame.after(100, self.track_color)
		elif self.current_feature == self.features[2]:
			print(self.path)

	def start_tracking(self):
		for w in self.rightbar.winfo_children():
			w.destroy()

		self.create_trackbar()
		self.update()		

	def print_val(self, event=None):
		for slider in self.slider_arr:
			print(slider.get(), end=' ')
		print()
		pass

	def track_color(self):
		if self.render_id:
			arr1 = [item.get() for item in self.slider_arr[:3]]
			arr2 = [item.get() for item in self.slider_arr[3:]]

			self.im = self.TDObj.detect_from_image(arr1, arr2)
			try:
				self.tracked_img['image'] = self.im
				self.update()
				self.render_id = self.imgFrame.after(100, self.track_color)
			except:
				print(self.path)

	def show_option(self):
		val = self.connection_option.get()
		if val == 1:
			self.server_label.grid_forget()
			self.server_entry.grid_forget()
			self.camera_label.grid(row=3, column=0, padx=10, pady=10)
			self.camera_entry.grid(row=4, column=0)
		elif val == 2:
			self.camera_label.grid_forget()
			self.camera_entry.grid_forget()
			self.server_label.grid(row=3, column=0, padx=10, pady=10)
			self.server_entry.grid(row=4, column=0)

		self.track_btn = tk.Button(self.rightbar, text='Track Color', width=10,
						relief=tk.RAISED, bg='dodgerblue3', fg='white',
						command=self.check_tracking)
		self.track_btn.grid(row=5, column=0, pady=20)

		self.imglabel = tk.Label(self.bottomBox)
		self.imglabel.grid(row=0, column=0)

		# self.canvas.destroy()
		self.tracked_img = tk.Label(self.imgFrame, bg='#afeeee')
		self.tracked_img.grid(row=0, column=0)
		self.update()

	def check_tracking(self):
		val = self.connection_option.get()
		dct = {1:self.camera_id, 2:self.server_id}
		self.path = dct.get(val, None)
		if self.path:
			self.path = self.path.get()
			self.track_btn.destroy()
			self.start_tracking()
			if val == 2:
				self.path = str(self.path) + '/shot.jpg'
			self.RTColorTracker = RealtimeColorTracker(self.path)
			self.track_color_from_stream()
		else:
			messagebox.showinfo('CoDAT', 'Enter the required value')

	def track_color_from_stream(self):
		val = self.connection_option.get()
		arr1 = [item.get() for item in self.slider_arr[:3]]
		arr2 = [item.get() for item in self.slider_arr[3:]]

		if val == 1:
			self.img = self.RTColorTracker.get_from_camera(arr1, arr2)
		else:
			self.img = self.RTColorTracker.get_from_stream(arr1, arr2)

		if len(self.img) == 2:
			orig, detected = self.img
			self.imglabel['image'] = orig
			self.tracked_img['image'] = detected
			self.imglabel.after(100, self.track_color_from_stream)
		elif self.img == "Cannot open camera":
			messagebox.showinfo('CoDAT', 'cannot initialize system camera')
			self.connection_option.set(0)
			self.set_selection(self.topbar.winfo_children()[2], self.features[2])
		elif self.img == "Cannot connect to stream":
			messagebox.showinfo('CoDAT', 'Cannot connect to stream. Check your network')
			self.connection_option.set(0)
			self.set_selection(self.topbar.winfo_children()[2], self.features[2])

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('700x450+350+130')
	root.title('CoDAT')

	app = Application(master=root)
	app.mainloop()