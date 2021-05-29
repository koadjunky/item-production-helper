from shopheroes.definitions import Quality
from shopheroes.hero import Hero, Item

heroes_list = [
    Hero.new('Azula', 44),
    Hero.new('Edward', 42),
    Hero.new('Mojian', 42),
    Hero.new('Francesca', 42),
    Hero.new('Oneira', 42),
    Hero.new('Darthos', 42),
    Hero.new('Louca', 41),
    Hero.new('Kuro Shobi', 41),
    Hero.new('Alicia', 41),
    Hero.new('Kurul', 41),
    Hero.new('Fiora', 41),
    Hero.new('Odette', 41),
    Hero.new('Irene', 41),
    Hero.new('Lancaster', 41),
    Hero.new('Mila', 40),
    Hero.new('Minh', 40),
    Hero.new('Clovis', 40),
    Hero.new('Albert', 40),
    Hero.new('Palash', 40),
    Hero.new('Gauvin', 40),
    Hero.new('Nya', 40),
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
#    probe_item(Item.new("Frostfire Blade", Quality.legendary))
#    probe_item(Item.new("Shattering Core", Quality.mythical))
#    probe_item(Item.new("Fire Smashers", Quality.legendary))    # Garbage
#    probe_item(Item.new("Obsidian Greaves", Quality.legendary))
#    probe_item(Item.new("Dragon Skull", Quality.legendary))     # Garbage
#    probe_item(Item.new("Demonic Visage", Quality.legendary))
#    probe_item(Item.new("Frostfire Shoes", Quality.legendary))
#    probe_item(Item.new("Obsidian Potion", Quality.legendary))

    probe_item(Item.new("Clarity Potion", Quality.legendary))
