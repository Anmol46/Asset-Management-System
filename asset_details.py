from tkinter import *
import tkinter as tk
import tkinter
from  tkinter import messagebox
import webbrowser
import pymysql

#This creates the main window of an application
window = tk.Tk()
window.title("Asset Details")
window.geometry("1350x750")
window.configure(background='mint cream')

def about(event):
    webbrowser.open_new("about.py")
    window.destroy()

def asset_details(event):
    webbrowser.open_new("asset_details.py")
    window.destroy()

def add_asset(event):
    webbrowser.open_new("add asset.py")
    window.destroy()

def issue_asset(event):
    webbrowser.open_new("issue_asset.py")
    window.destroy()

def return_asset(event):
    webbrowser.open_new("return_asset.py")
    window.destroy()

#Title
w = tk.Label(window,background='mint cream')
w.pack()
w = tk.Label(window,background='mint cream', text = "Asset Tracking System",font=('arial',30,'bold'),fg='gold')
w.pack()

w = Frame (window , bg = 'cyan' )
w.place(x = 25 , y = 100, width = 1310, height = 30)


link = Label(window, text="About",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 20 , y = 100, width = 50, height = 30)
link.bind("<Button-1>", about)


link = Label(window, text="Asset Details",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 70 , y = 100, width = 90, height = 30)
link.bind("<Button-1>", asset_details)


link = Label(window, text="Add Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 165 , y = 100, width = 70, height = 30)
link.bind("<Button-1>", add_asset)


link = Label(window, text="Issue Assset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 235 , y = 100, width = 100, height = 30)
link.bind("<Button-1>", issue_asset)


link = Label(window, text="Return Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 330 , y = 100, width = 100, height = 30)
link.bind("<Button-1>", return_asset)


conn = pymysql.connect(host='localhost',user='root',password='',db='iot')

a = conn.cursor()
a.execute("SELECT * FROM asset")

row = a.fetchall()

title1 = Label(window, text = 'Barcode Number', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 425, y = 250 , width=160, height=25)

title1 = Label(window, text = 'Asset Name', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 625, y = 250 , width=160, height=25)

title1 = Label(window, text = 'Description', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 825, y = 250 , width=160, height=25)


q = 300
while row is not None:
    for i in range(len(row)):
        p = 225
        for j in range(0,4):
            p = p + 200
            title1 = Label(window, text = row[i][j], font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
            title1.place(x = p, y = q , width=160, height=25)
        q = q + 50
    break



conn.close()

window.mainloop()
