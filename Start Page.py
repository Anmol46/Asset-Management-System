from tkinter import *
import webbrowser
import tkinter as tk
from PIL import Image
from PIL import ImageTK


#This creates the main window of an application
window = tk.Tk()
window.title("Asset Tracking System")
window.geometry("1350x750")
window.configure(background='white')

def callback(event):
    webbrowser.open_new("about.py")
    window.destroy()

#Image
path = "background.jpg"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))
#img = tk.PhotoImage(file="/home/pi/Desktop/IoT/background.jpg")
img = ImageTk.PhotoImage(Image.open(path))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Title
w = tk.Label(window,background='azure', text = "Asset Tracking System",font=('arial',30,'bold'),fg='gold')
w.place(x = 115 , y = 535, width = 450, height = 50)



link = Label(window, text="Click Here To Continue", fg="blue", cursor="hand2")
link.place(x = 115 , y = 600, width = 150, height = 40)
link.bind("<Button-1>", callback)




#Start the GUI
window.mainloop()
