from shopheroes.definitions import Quality
from shopheroes.hero import Hero


if __name__ == '__main__':
    hero = Hero.new('Kuro Shobi', 43)
    iset = hero.ideal_set(Quality.mythical)
    for type, items in iset.items():
        print(type)
        for item in items:
            if item[1] == 0.0:
                print("    {} {}".format(item[0], item[2]))

