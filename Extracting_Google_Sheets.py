
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Quickstart.json", scope)

client = gspread.authorize(creds)

sheet = client.open('Ibrahim').sheet1

data = sheet.get_all_records()

cell = sheet.cell(2,3).value #You can always add more more cell variables you need to read within the virtual Assistant.py