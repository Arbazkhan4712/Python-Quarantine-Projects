from tkinter import *
import youtube_dl
root=Tk()

root.title('Youtube downloader')
root.geometry("370x23")
ydl_opts = {}
def download():
    link_of_the_video = text_box.get()
    zxt = link_of_the_video.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])


text_box=Entry(root,width=50)
text_box.insert(string="paste link here...",index=1)
button=Button(root,text='Download',command=download)
text_box.grid(row=0,column=0)
button.grid(row=0,column=1)



root.mainloop()
