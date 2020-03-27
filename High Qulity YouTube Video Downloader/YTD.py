from tkinter import *
import youtube_dl
root=Tk()
root.title('HD Youtube Video downloader')
root.iconbitmap(r"yt.ico")
root.resizable(False,False)
width = 500
height = 200
root.config(bg="indian red")
# to get the screen in the center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

ydl_opts = {}
def download():
    link_of_the_video = e1.get()
    zxt = link_of_the_video.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])
def some_callback(event):
    if e1.get() == "paste link here..":
        e1.delete(0, "end")
lbl1 = Label(root,text="Download Videos with One-Click", fg="black",bg="indian red" ,font=('arial', 16)).place(x=15, y=40)
e1= Entry(root)
e1.config(font=('arial', 14), width=27)
e1.insert(END, "paste link here..")
e1.bind("<Button-1>", some_callback)
e1.place(x=20, y=100)
button=Button(root,text='Download', bg="indianred3", fg="black", font=('arial', 16), command=download).place(x=350,y=90)
root.mainloop()