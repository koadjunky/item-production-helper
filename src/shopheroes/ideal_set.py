from shopheroes.definitions import Quality, types, items_list, Craft
from shopheroes.hero import Hero, Item


def ideal_set(hero : Hero, quality : Quality):
    result = {}
    for type in types:
        result[type] = []
        for eq_def in hero.hero_def.eq_defs:
            if eq_def.type != type:
                continue
            for item_def in items_list:
                if item_def.klass != eq_def.klass:
                    continue
                if item_def.craft > Craft.COMMON:
                    continue
                for q in Quality:
                    if q > quality:
                        continue
                    item = Item(item_def, q)
                    if not hero.can_equip(item):
                        continue
                    break_chance = item.break_chance(hero)
                    damage = item.item_def.power[q]
                    result[type].append((item, break_chance, damage))
        result[type].sort(key=lambda x: 100000000 * x[1] - x[2])
    return result


if __name__ == '__main__':
    hero = Hero.new('Karal', 30)
    iset = ideal_set(hero, Quality.legendary)
    for type, items in iset.items():
        print(type)
        for item in items:
            if item[1] == 0.0:
                print("    {} {}".format(item[0], item[2]))

