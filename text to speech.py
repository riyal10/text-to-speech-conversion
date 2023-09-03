from tkinter import *#importing everything from module
from tkinter import messagebox#for pop up of message
import pyttsx3

engine = pyttsx3.init()#initializing of pyttsx3 module
win = Tk()#for making the window or platform
win.title(" text to voice converter")#for title name
win.configure(bg="yellow")#for changing screen or background color
win.geometry("420x200")#for increasing or decreasing size of the window 

def speak():#declaration of function
    t=entry1.get()
    engine.setProperty("rate",150)
    engine.say(t)#conversion of text to voice
    engine.runAndWait()#conversion of text to voice and then exit the program
    engine.stop()
    if(t==""):#if user does not enter any text
        messagebox.showerror("Error","Please enter the text")

#Label frame
lf = LabelFrame(win,text="Text to Voice",font="30",bd=5,bg="pink")
lf.pack(fill="both",expand="yes",padx=10,pady=10)
Label(lf,text="Text",font="30",bd=5,padx=15).pack(side=LEFT)

#entry----user enters the text
text=StringVar()#for fetching of text entered by user
entry1=Entry(lf,width=25,bd=5,font="20",textvariable=text)
entry1.pack(side=LEFT,padx=10)

#button
Button(lf,text="Voice",font=15,command=speak).pack(side=LEFT)

mainloop()#window will remain open
