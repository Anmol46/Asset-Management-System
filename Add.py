import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
client = gspread.authorize(creds)
sh = client.open('abhishek')
sheet = sh.get_worksheet(0)


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
