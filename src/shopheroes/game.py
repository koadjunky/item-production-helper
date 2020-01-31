from shopheroes.definitions import Quality
from shopheroes.hero import Hero, Item

heroes_list = [
    Hero.new('Azula', 42),
    Hero.new('Edward', 40),
    Hero.new('Mojian', 40),
    Hero.new('Francesca', 40),
    Hero.new('Oneira', 40),
    Hero.new('Darthos', 39),
    Hero.new('Nya', 40),
    Hero.new('Louca', 39),
    Hero.new('Kuro Shobi', 39),
    Hero.new('Alicia', 39),
    Hero.new('Kurul', 39),
    Hero.new('Fiora', 38),
    Hero.new('Odette', 39),
    Hero.new('Irene', 39),
    Hero.new('Mila', 38),
    Hero.new('Lancaster', 39),
    Hero.new('Minh', 38),
    Hero.new('Clovis', 38),
    Hero.new('Gauvin', 38),
    Hero.new('Albert', 38),
    Hero.new('Palash', 38),
    Hero.new('Theor', 35),
    Hero.new('Garreth', 35),
    Hero.new('Karal', 30),
    Hero.new('Melina', 30)
]

heroes = {hero.hero_def.name: hero for hero in heroes_list}


def probe_low_quality_item(item : Item):
    result = {}
    for hero in heroes_list:
        if hero.can_equip(item):
            result[hero] = item.break_chance(hero)
    return result


def probe_high_quality_item(item : Item):
    result = {}
    for hero in heroes_list:
        levels = item.number_of_levels_until_unbreakable(hero)
        if levels >= 0:
            result[hero] = levels
    return result


def probe_item(item : Item):
    print("Examining {}".format(item))
    if item.quality > Quality.flawless:
        eglible_heroes = sorted(probe_high_quality_item(item).items(), key=lambda it : it[1])
        if len(eglible_heroes) == 0:
            print("    Nobody can use it anymore. Sell it!")
        for hero, level in eglible_heroes:
            print("    {} can use item in {} levels".format(hero, level))
    else:
        for hero, chance in sorted(probe_low_quality_item(item).items(), key=lambda it : it[1]):
            print("    {} can use item with {} break chance".format(hero, chance))


if __name__ == '__main__':
    item = Item.new("Hell Hound", Quality.epic)
    probe_item(item)
