import os.path
import jsons
from oauth2client.service_account import ServiceAccountCredentials
import gspread

from shopheroes.gspread_formatting_utils import get_effective_formats
from shopheroes.definitions import ItemDef
from shopheroes.definitions import HeroDef
from shopheroes.definitions import EqDef


def number2int(power):
    return int(power.replace(',', ''))

# Type: Weapon
#   Klass: Swords, Daggers, Axes, Spears, Maces, Staves, Bows, Guns
# Type: Chest
#   Klass: Armor, Vests, Clothes
# Type: Head
#   Klass: Helmets, Hats
# Type: Arm
#   Klass: Gauntlets, Bracers
# Type: Leg
#   Klass: Boots, Footwear
# Type: Accessory
#   Klass: Shields, Rings, Pendants, Instruments
# Type: Valuable
#   Klass: Spells, Potions, Remedies, Projectiles


class ShopHeroesDataSpreadsheet:

    SCOPES = ['https://spreadsheets.google.com/feeds']
    KEYFILE = 'shopheroes-259822-947b9230a56b.json'
    SHEET_URL = 'https://docs.google.com/spreadsheets/d/1yOLklDGX2LmndWKvQuRYkAOO0WqHsudv8kvEhLWx_so/edit#gid=0'

    def __init__(self):
        libdir = os.path.dirname(os.path.realpath(__file__))
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
            power = {
                'base': number2int(row[3]),
                'good': number2int(row[45]),
                'great': number2int(row[46]),
                'flawless': number2int(row[47]),
                'epic': number2int(row[48]),
                'legendary': number2int(row[49]),
                'mythical': number2int(row[50])
            }
            item_def = ItemDef(row[1], row[2], row[4], power)
            result.append(item_def)

        return result

    def get_heroes_power(self):
        powers_wk = self.get_worksheet('Hero Levels & Power')
        powers = powers_wk.get_all_values()

        result = {}
        for i in range(28):
            name = powers[i+1][5]
            power_start = number2int(powers[i+1][7])
            power_multi = float(powers[i+1][6])
            result[name] = {'start': power_start, 'multi': power_multi}
        return result

    @staticmethod
    def get_affinity(x, y, formats):
        bg = formats[y][x].backgroundColor.green
        if bg == 0.7607843:
            return -0.025
        elif bg == 0.91764706:
            return 0
        elif bg == 0.8980392:
            return 0.0125
        elif bg == 0.8:
            return 0.025
        else:
            raise Exception("Unknown background green component {} in cell ({}, {})".format(bg, x+1, y+1))

    @staticmethod
    def get_hero_equipment(x, y, values, formats):
        result = []
        if values[y][x] == '':
            return result
        for i in range(7):
            for j in range(4):
                if values[y+3+j][x+i] != '---':
                    type_ = values[y+2][x+i]
                    klass = values[y+3+j][x+i]
                    affinity = ShopHeroesDataSpreadsheet.get_affinity(x+i, y+3+j, formats)
                    eq_def = EqDef(klass, type_, affinity)
                    result.append(eq_def)
        return result

    def get_heroes(self):
        powers = self.get_heroes_power()
        heroes_wk = self.get_worksheet('Heroes')
        values = heroes_wk.get_all_values()
        formats = get_effective_formats(heroes_wk)

        result = []
        for i in [1, 12, 23]:
            for j in [1, 9, 17, 25, 33, 41, 49, 57, 65, 73]:
                name = values[j][i].lower().title()
                if name != '':
                    lmax = int(values[j][i+3])
                    power_start = powers[name]['start']
                    power_multi = powers[name]['multi']
                    eq_defs = self.get_hero_equipment(i, j, values, formats)
                    hero_def = HeroDef(name, lmax, power_start, power_multi, eq_defs)
                    result.append(hero_def)

        return result


if __name__ == '__main__':
    ts = ShopHeroesDataSpreadsheet()
    print(jsons.dumps(ts.get_items(), jdkwargs={"indent": 4}))
    print(jsons.dumps(ts.get_heroes(), jdkwargs={"indent": 4}))
