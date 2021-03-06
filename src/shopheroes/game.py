from shopheroes.definitions import Quality
from shopheroes.hero import Hero, Item

heroes_list = [
    Hero.new('Azula', 43),
    Hero.new('Edward', 41),
    Hero.new('Mojian', 41),
    Hero.new('Francesca', 41),
    Hero.new('Oneira', 40),
    Hero.new('Darthos', 40),
    Hero.new('Nya', 40),
    Hero.new('Louca', 40),
    Hero.new('Kuro Shobi', 39),
    Hero.new('Alicia', 39),
    Hero.new('Kurul', 40),
    Hero.new('Fiora', 39),
    Hero.new('Odette', 40),
    Hero.new('Irene', 40),
    Hero.new('Mila', 39),
    Hero.new('Lancaster', 39),
    Hero.new('Minh', 40),
    Hero.new('Clovis', 39),
    Hero.new('Gauvin', 39),
    Hero.new('Albert', 39),
    Hero.new('Palash', 39),
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
#    probe_item(Item.new("Frostfire Blade", Quality.epic))
#    probe_item(Item.new("Skofnung", Quality.epic))
#    probe_item(Item.new("Obsidian Voulge", Quality.epic))
#    probe_item(Item.new("Ascalon", Quality.epic))
#    probe_item(Item.new("Shattering Core", Quality.mythical))
#    probe_item(Item.new("Keeper of Souls", Quality.epic))
#    probe_item(Item.new("Blaster", Quality.epic))
#    probe_item(Item.new("Pirate Pistol", Quality.epic))
#    probe_item(Item.new("Earthen Mail", Quality.epic))
#    probe_item(Item.new("Earthen Mail", Quality.mythical))
#    probe_item(Item.new("Ocean Leather", Quality.epic))
#    probe_item(Item.new("Frostfire Barbuta", Quality.epic))
#    probe_item(Item.new("Berserker Gauntlets", Quality.epic))
#    probe_item(Item.new("Obsidian Greaves", Quality.epic))
#    probe_item(Item.new("King's Mantle", Quality.epic))
#    probe_item(Item.new("Hawk Shield", Quality.epic))
#    probe_item(Item.new("Medusa Buckler", Quality.epic))
#    probe_item(Item.new("Dragon Skull", Quality.legendary))
#    probe_item(Item.new("Cultist's Hood", Quality.epic))
#    probe_item(Item.new("Frostfire Shoes", Quality.epic))
#    probe_item(Item.new("Draconic Tea", Quality.epic))
#    probe_item(Item.new("Devil Dust", Quality.epic))
#    probe_item(Item.new("Obsidian Potion", Quality.legendary))
#    probe_item(Item.new("Obsidian Potion", Quality.epic))
#    probe_item(Item.new("Unholy Potion", Quality.epic))
#    probe_item(Item.new("Haunted Scroll", Quality.epic))
#    probe_item(Item.new("Frostfire Kunai", Quality.epic))
#    probe_item(Item.new("Frostfire Harp", Quality.epic))
#    probe_item(Item.new("Wyrm Horn", Quality.epic))
