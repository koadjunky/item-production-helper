from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os.path
libdir = os.path.dirname(os.path.realpath(__file__))


class ShopHeroesDataSpreadsheet:

    SCOPES = ['https://spreadsheets.google.com/feeds']
    KEYFILE = 'shopheroes-259822-947b9230a56b.json'
    SHEET_URL = 'https://docs.google.com/spreadsheets/d/1yOLklDGX2LmndWKvQuRYkAOO0WqHsudv8kvEhLWx_so/edit#gid=0'

    def __init__(self):
        keyfile = os.path.join(libdir, 'resources', self.KEYFILE)
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, self.SCOPES)
        self.gc = None
        self.sheet = None
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
        heroes_wk = self.get_worksheet('Heroes')
        heroes = heroes_wk.get_all_values()

        powers_wk = self.get_worksheet('Hero Levels & Power')
        powers = powers_wk.get_all_values()

        result = {}
        for i in [1, 12, 23]:
            for j in [1, 9, 17, 25, 33, 41, 49, 57, 65, 73]:
                record = {
                    'name': heroes[j][i].lower().title(),
                    'level': heroes[j][i+3],
                    'power': 0,
                    'multi': 0,

                }
                if record['name'] != '':
                    result[record['name']] = record
        for i in range(28):
            result[powers[i+1][5]]['multi'] = powers[i+1][6]
            result[powers[i+1][5]]['power'] = powers[i+1][7]

        return result

    def get_equipment(self):
        worksheet = self.get_worksheet('Heroes')
        values = worksheet.get_all_values()
        result = list()
        for i in [1, 12, 23]:
            for j in [1, 9, 17, 25, 33, 41, 49, 57, 65, 73]:
                result.append(self.get_hero_equipment(i, j, values))
        return result

    @staticmethod
    def get_hero_equipment(x, y, values):
        result = []
        if values[y][x] == '': return result
        for i in range(7):
            for j in range(4):
                if values[y+3+j][x+i] != '---':
                    record = {
                        'name': values[y][x].lower().title(),
                        'type': values[y+2][x+i],
                        'item': values[y+3+j][x+i],
                        'affinity': 0,
                    }
                    result.append(record)
        return result


if __name__ == '__main__':
    import pprint
    ts = ShopHeroesDataSpreadsheet()
    pprint.pprint(ts.get_equipment())
