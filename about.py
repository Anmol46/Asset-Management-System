from tkinter import *
import tkinter as tk
import tkinter
from  tkinter import messagebox
import webbrowser

#This creates the main window of an application
window = tk.Tk()
window.title("Asset Tracking System")
window.geometry("1350x750")
window.configure(background='mint cream')

def callback(event):
    webbrowser.open_new("Start Page.py")

#Title
w = tk.Label(window,background='mint cream')
w.pack()
w = tk.Label(window,background='mint cream', text = "Asset Tracking System",font=('arial',30,'bold'),fg='gold')
w.pack()

w = Frame (window , bg = 'cyan' )
w.place(x = 25 , y = 100, width = 1310, height = 30)


link = Label(window, text="About",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 20 , y = 100, width = 50, height = 30)
link.bind("<Button-1>", callback)

link = Label(window, text="Asset Details",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 70 , y = 100, width = 70, height = 30)
link.bind("<Button-1>", callback)

link = Label(window, text="Add Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 145 , y = 100, width = 60, height = 30)
link.bind("<Button-1>", callback)

link = Label(window, text="Issue Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 205 , y = 100, width = 75, height = 30)
link.bind("<Button-1>", callback)

link = Label(window, text="Return Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 280 , y = 100, width = 70, height = 30)
link.bind("<Button-1>", callback)


window.mainloop()
