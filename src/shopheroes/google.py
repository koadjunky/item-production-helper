import os.path
libdir = os.path.dirname(os.path.realpath(__file__))

from oauth2client.service_account import ServiceAccountCredentials
import gspread



class ShopHeroesDataSpreadsheet:

    SCOPES = ['https://spreadsheets.google.com/feeds']
    KEYFILE = 'shopheroes-259822-947b9230a56b.json'
    SHEET_URL = 'https://docs.google.com/spreadsheets/d/1yOLklDGX2LmndWKvQuRYkAOO0WqHsudv8kvEhLWx_so/edit#gid=0'

    def __init__(self):
        keyfile = os.path.join(libdir, 'resources', self.KEYFILE)
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, self.SCOPES)
        self.connect()

    def connect(self):
        self.gc = gspread.authorize(self.credentials)
        self.sheet = self.gc.open_by_url(self.SHEET_URL)

    def get_worksheet(self, name):
        try:
            return self.sheet.worksheet(name)
        except gspread.exceptions.APIError:
            self.connect()
            return self.sheet.worksheet(name)

    def get_items(self):
        worksheet = self.get_worksheet('Item Directory')
        values = worksheet.get_all_values()

        result = []
        for row in values[1:]:
            record = {
                'name': row[1],
                'level': row[2],
                'class': row[4],
                'base': row[3],
                'good': row[45],
                'great': row[46],
                'flawless': row[47],
                'epic': row[48],
                'legendary': row[49],
                'mythical': row[50]
            }
            result.append(record)

        return result

    def get_heroes(self):
        worksheet = self.get_worksheet('Heroes')
        values = worksheet.get_all_values()

        result = []
        record = {
            'name': values[1][1]
        }
        result.append(record)

        return result


if __name__ == '__main__':
    import pprint
    ts = ShopHeroesDataSpreadsheet()
    pprint.pprint(ts.get_heroes())
