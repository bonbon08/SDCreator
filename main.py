import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *
import os

def openone():
    entry4.delete(0,END)
    file = askopenfilename()
    entry4.insert(10,file)
def opentwo():
    entry5.delete(0,END)
    file = askopenfilename()
    entry5.insert(10,file)
def install():
    home=os.environ["HOME"]
    print(home)
    Appname=entry1.get()
    versionnumber=entry2.get()
    Typetype=entry6.get()
    apppath=entry4.get()
    iconpath=entry5.get()
    test=var1.get()
    termistrue="true"
    if test==1:
        termistrue="true"
    elif test==0:
        termistrue="false"
    data1 = open(home + "/.local/share/applications/" + Appname + ".desktop", "x")
    print("Done 1")
    data1.write("[Desktop Entry]\n")
    print("Done 1")
    data1.write("Encoding=UTF-8\n")
    print("Done 1")
    data1.write("Version=" + versionnumber + "\n")
    print("Done 1")
    data1.write("Type=" + Typetype + "\n")
    print("Done 1")
    data1.write("Terminal=" + termistrue + "\n")
    print("Done 1")
    data1.write("Exec=" + apppath + "\n")
    print("Done 1")
    data1.write("Name=" + Appname + "\n")
    print("Done 1")
    data1.write("Icon=" + iconpath + "\n")
    print("Done 1")
    data1.close()
    messagebox.showinfo("100%", "installation done")

Buttonfarbe="white"
Hintergrundfarbe="white"
eingabefarbe="white"

app= Tk()
app.title("Auto-.desktop")
app.config(width=375, height=425)
anzeige1 = Label(app, text = "Auto-.desktop")
anzeige1.place(x = 20 , y = 20)
anzeige2 = Label(app, text = "Appname:")
anzeige2.place(x = 20 , y = 50)
entry1 = Entry(app, width=40)
entry1.place(x = 20 , y = 80)#place(x=80, y=10, width=460, height=30)
anzeige3 = Label(app, text = "Versionnumber:")
anzeige3.place(x = 20 , y = 110)
entry2 = Entry(app, width=40)
entry2.place(x = 20 , y = 140)#place(x=80, y=10, width=460, height=30)
anzeige7 = Label(app, text = "Type of Application:")
anzeige7.place(x = 20 , y = 170)
entry6 = Entry(app, width=40)
entry6.place(x = 20 , y = 200)#place(x=80, y=10, width=460, height=30)
anzeige5 = Label(app, text = "Path to execouteble:")
anzeige5.place(x = 20 , y = 230)
Button2 = Button(app, text="Search" ,command=openone)
Button2.place(x = 20 , y = 260)
entry4 = Entry(app, width=25)
entry4.place(x = 140 , y = 260)#place(x=80, y=10, width=460, height=30)
anzeige6 = Label(app, text = "Path to icon:")
anzeige6.place(x = 20 , y = 290)
Button3 = Button(app, text="Search", command=opentwo)
Button3.place(x = 20 , y = 320)
entry5 = Entry(app, width=25)
entry5.place(x = 140 , y = 320)#place(x=80, y=10, width=460, height=30)
var1 = IntVar()
checkbutton1=Checkbutton(app, text="Run in Terminal", variable=var1)
checkbutton1.place(x = 20 , y = 350)
Button1 = Button(app, text="Install" ,command=install)
Button1.place(x = 20 , y = 380)
app.mainloop()