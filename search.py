import gspread
from oauth2client.service_account import ServiceAccountCredentials

print("Scan the Barcode")
bno = int(input())
print("\n")

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('12345.json',scope)
client = gspread.authorize(creds)
sh = client.open('abhishek')
sheet = sh.get_worksheet(0)

r = 8
c = 4


#row=1

def search():
    for i in range(2,r+1):
        k = 1
        a = sheet.cell(i,k).value
        if(bno == int(a)):
            print("\n")
            print("Barcode No  : "+sheet.cell(i,1).value)
            print("Name : "+sheet.cell(i,2).value)
            print("Description : "+sheet.cell(i,3).value)
            print("Status : "+sheet.cell(i,4).value)
            return

search()


            
#for k in range(1,c+1):
    #print(sheet.cell(a,k).value)


