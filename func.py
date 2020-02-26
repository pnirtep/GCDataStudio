from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1JdPwwwaUnqv2WYVVn9DQeFIu017zWHh7Go5dMQvLEek'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)



# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='ЛИСТ1',
    majorDimension='COLUMNS'
).execute()
pprint(values)
cell_list = values['values']
print(cell_list)
cells = cell_list[0]
print(cells)
cell = len(cells)
print(cell)

def sheet_write(data):
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "ЛИСТ1!A"+str(cell+1),
             "majorDimension": "ROWS",
             "values": [[data[0], data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[8]]]}
            ]
        }
    ).execute()
    return