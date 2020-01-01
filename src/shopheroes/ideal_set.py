from shopheroes.definitions import Quality
from shopheroes.hero import Hero


if __name__ == '__main__':
    hero = Hero.new('Karal', 30)
    iset = hero.ideal_set(Quality.legendary)
    for type, items in iset.items():
        print(type)
        for item in items:
            if item[1] == 0.0:
                print("    {} {}".format(item[0], item[2]))

