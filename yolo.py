import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
client = gspread.authorize(creds)
sh = client.open('abhishek')
sheet = sh.get_worksheet(0)

r = 10
c = 4

for i in range(1,r+1):
    for j in range(1,c+1):
        #p = sheet.cell(i,j).value
        p = sheet.row_slice(i)
        print(p)
