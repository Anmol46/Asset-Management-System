import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
client = gspread.authorize(creds)
sh = client.open('abhishek')
sheet = sh.get_worksheet(0)


r = 5
c = 4
#id = 123456789
#name = "Parth Kothari"
#row = 2
#col = 2


print("Scan The Barcode")
bno = float(input())

issue = "Available"

#status = "Available"
#row = [bno,n,desc,status]
#index = 2
#sheet.insert_row(row,index)

#row = 2
#col = 2


def search():
    for i in range(2,r+1):
        k = 1
        a = sheet.cell(i,k).value
        if(bno == int(a)):
            sheet.update_cell(i ,4 ,issue)
            return


search()    
print("Sheet Updated")
