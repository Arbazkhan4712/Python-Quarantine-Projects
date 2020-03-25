from tkinter import *
import youtube_dl
root=Tk()

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