from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import youtube_dl
import os
root=tk.Tk()
root.title('Youtube downloader V-2.1')
root.geometry("350x140")
root.config(bg='#dfe6e9')
ydl_opts = {}
def shutcom():
    global key
    key=0
    buttonshut = tk.Button(root, text="yes", command=shutcom,state=DISABLED,bg='#dfe6e9',fg= '#f2f2f2')
    buttonshut.grid(row=4, column=1)
def download(link):
    link_of_the_video = link
    zxt = link_of_the_video.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])


def downloadall():
    for i in range(4):
        if i==0 :
            if text1.get()!='paste link 1 here...':
                pro1.start()
                download(text1.get())
                pro1.destroy()
                lable1=Label(root,text='completed!').grid(row=0,column=1)
                

        if i==1:

            if text2.get() != 'paste link 2 here...':
                
                pro2.start()
                
                download(text2.get())
                pro2.destroy()
                lable2 = Label(root, text='completed!').grid(row=1, column=1)

        if i==2:
            if text3.get() != 'paste link 3 here...':
                
                pro3.start()
                
                download(text3.get())
                pro3.destroy()
                lable3 = Label(root, text='completed!').grid(row=2, column=1)

        if i==3:
            if text4.get() != 'paste link 4 here...':
                
                pro4.start()
                
                download(text4.get())
                pro4.destroy()
                lable4 = Label(root, text='completed!').grid(row=3, column=1)


    if key==0:
        os.system("shutdown /s /t 1")


key=1
text1=tk.Entry(root,width=50,bg='#dfe6e9',fg='#0984e3')
text2=tk.Entry(root,width=50,bg='#dfe6e9',fg='#0984e3')
text3=tk.Entry(root,width=50,bg='#dfe6e9',fg='#0984e3')
text4=tk.Entry(root,width=50,bg='#dfe6e9',fg='#0984e3')

text1.insert(string='paste link 1 here...',index=1)
text2.insert(string='paste link 2 here...',index=1)
text3.insert(string='paste link 3 here...',index=1)
text4.insert(string='paste link 4 here...',index=1)
button=tk.Button(root,text='download all',command=downloadall,bg='#dfe6e9',fg= '#0984e3')
button.config(highlightbackground='#f2f2f2')
shutlabel=tk.Label(root,text="do you want to shutdown after all downloads:",bg='#dfe6e9',fg= '#0984e3')
buttonshut=tk.Button(root ,text="yes",command=shutcom,bg='#dfe6e9',fg= '#0984e3')

text1.grid(row=0,column=0,columnspan=2)
text2.grid(row=1,column=0,columnspan=2)
text3.grid(row=2,column=0,columnspan=2)
text4.grid(row=3,column=0,columnspan=2)
button.grid(row=5,column=0)
shutlabel.grid(row=4,column=0)
buttonshut.grid(row=4,column=1)

pro1=Progressbar(root,length = 100,orient=HORIZONTAL,mode='indeterminate')
pro1.grid(row=0,column=1)
pro2=Progressbar(root,length = 100,orient=HORIZONTAL,mode='indeterminate')
pro2.grid(row=1,column=1)
pro3=Progressbar(root,length = 100,orient=HORIZONTAL,mode='indeterminate')
pro3.grid(row=2,column=1)
pro4=Progressbar(root,length = 100,orient=HORIZONTAL,mode='indeterminate')
pro4.grid(row=3,column=1)



root.mainloop()

