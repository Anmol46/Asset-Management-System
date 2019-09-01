print("Welcome To Asset Management System")

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
client = gspread.authorize(creds)
sh = client.open('abhishek')
sheet = sh.get_worksheet(0)

choice=1
while(choice !=5):
    print("\n**** MENU ****")
    print("1 : Add Asset")
    print("2 : Search Asset")
    print("3 : Issue Asset")
    print("4 : Return Asset")
    print("5 : Exit")

    print("\n\nEnter Your Choice : ")
    choice = int(input())

    if(choice == 9780201371116):
        print("\nAdd Asset")
        print("Scan The Barcode")
        bno = float(input())

        print("Asset Name")
        n = raw_input()

        print("Decription")
        desc = raw_input()

        status = "Available"
        row = [bno,n,desc,status]
        index = 2
        sheet.insert_row(row,index)
        print("Sheet Updated")

    elif(choice == 9780201373578):
        print("\nSearch Asset")
        print("Scan the Barcode")
        bno = int(input())
        r = 8
        c = 4
        for i in range(2,r+1):
            k = 1
            a = sheet.cell(i,k).value
            if(bno == int(a)):
                print("\n")
                print("Barcode No  : "+sheet.cell(i,1).value)
                print("Name : "+sheet.cell(i,2).value)
                print("Description : "+sheet.cell(i,3).value)
                print("Status : "+sheet.cell(i,4).value)
                break
   
    elif(choice == 9780201379518):
        r = 5
        c = 4
        print("\nIssue Asset")
        print("Scan The Barcode")
        bno = float(input())

        print("Issue To ")
        issue = raw_input()

        for i in range(2,r+1):
            k = 1
            a = sheet.cell(i,k).value
            if(bno == int(a)):
                sheet.update_cell(i ,4 ,"Issued To " +issue)
        print("Sheet Updated")

    elif(choice == 9780201374360):
        r = 5
        c = 4
        print("\nReturn Asset")
        print("Scan The Barcode")
        bno = float(input())

        issue = "Available"
        for i in range(2,r+1):
            k = 1
            a = sheet.cell(i,k).value
            if(bno == int(a)):
                sheet.update_cell(i ,4 ,issue)
                
    else:
        break

