import datetime
from pytz import timezone
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheets:
    '''
    Sheets class to interact with budget workbook
    '''

    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    def addExpense(self, amount, description, category, method):
        sheet = self.client.open('Budget').sheet1
        
        date = str(datetime.date.today().strftime('%M/%D/%Y'))
        time = str(datetime.datetime.now(timezone('US/Eastern'))\
                    .strftime('%H:%M:%S')) 

        newRow = [date,
                time,
                amount,
                description,
                category,
                method]

        sheet.append_row(newRow, value_input_option='USER_ENTERED')
