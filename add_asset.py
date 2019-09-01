import tkinter as tk
import tkinter
from  tkinter import messagebox
import webbrowser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random


#This creates the main window of an application
window = tk.Tk()
window.title("Add Asset")
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
    
def generate_barcode(event):
    num=random.randrange(1,1000000000000)
    print(num)
    image=barcode.get_barcode_class('ean13')
    image_bar=image(u'{}'.format(num))
    file=open('/home/pi/Desktop/b.svg','wb')
    image_bar.write(file)
    messagebox.showinfo("Alert", "New Barcode stored at location 'D:\\barcode.svg'")

def asset_detail(event):
    webbrowser.open_new("asset_details.py")
    window.destroy()
    
#Submit Button Code
def SubmitButton():
    id = e1.get()
    name = e2.get()
    desc = e3.get()
    print("gaya")
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
    client = gspread.authorize(creds)
    sh = client.open('abhishek')
    sheet = sh.get_worksheet(0)
    id=123
    row = [id]
    index = 1
    sheet.insert_row(row,index)


    
    
#Title
w = tk.Label(window,background='mint cream')
w.pack()
w = tk.Label(window,background='mint cream', text = "Asset Tracking System",font=('arial',30,'bold'),fg='gold')
w.pack()

w = tk.Frame (window , bg = 'cyan' )
w.place(x = 25 , y = 100, width = 1310, height = 30)


link = tk.Label(window, text="About",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 20 , y = 100, width = 50, height = 30)
link.bind("<Button-1>", about)


link = tk.Label(window, text="Asset Details",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 70 , y = 100, width = 90, height = 30)
link.bind("<Button-1>", asset_detail)


link = tk.Label(window, text="Add Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 165 , y = 100, width = 70, height = 30)
link.bind("<Button-1>", add_asset)


link = tk.Label(window, text="Issue Assset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 235 , y = 100, width = 100, height = 30)
link.bind("<Button-1>", issue_asset)


link = tk.Label(window, text="Return Asset",bg = 'cyan', fg="blue", cursor="hand2")
link.place(x = 330 , y = 100, width = 100, height = 30)
link.bind("<Button-1>", return_asset)


link = tk.Label(window, text="Add Asset",font=('arial',25,'bold'), fg="blue", cursor="hand2")
link.place(x = 580 , y = 170, width = 175, height = 30)

title1 = tk.Label(window,text = 'Barcode No', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 500, y = 225 , width=120, height=25)
e1 = tk.Entry(window)
e1.place(x = 650 , y = 225, width = 150, height = 25)
link = tk.Label(window, text="Generate Barcode",background = 'mint cream', fg="blue", cursor="hand2")
link.place(x = 810 , y = 225, width = 120, height = 25)
link.bind("<Button-1>", generate_barcode)

title1 = tk.Label(window, text = 'Asset Name', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 500, y = 275 , width=120, height=25)
e2 = tk.Entry(window)
e2.place(x = 650 , y = 275, width = 150, height = 25)

title1 = tk.Label(window, text = 'Description', font = ('arial',15),fg = 'blue',background = 'mint cream',anchor = 'w')
title1.place(x = 500, y = 325 , width=150, height=25)
e3 = tk.Entry(window)
e3.place(x = 650 , y = 325, width = 150, height = 25)


B = tkinter.Button(window, text ="Submit", command=SubmitButton)
B.place(x =600 , y = 375 , width = 80, height = 25)


window.mainloop()
