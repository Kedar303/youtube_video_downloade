from tkinter import *
from tkinter import messagebox as msg

def download():
        from pytube import YouTube
        url = str(k.get())
        x = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        x.download()
        msg.showinfo("Done","Video downloaded successfully")
        
        



root = Tk()
root.title("YouTube video downloader")
root.geometry("400x200")

r = Label(root,text = "Enter video link",font="Trebuchet")
r.place(x=130,y=10)
k = Entry(root,bd=5,font="Trebuchet")
k.place(x=90,y=50)
b = Button(root,text="Download",font="Trebuchet",command=download)
b.place(x=150,y=100)
