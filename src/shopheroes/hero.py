from shopheroes.definitions import heroes_dict, items_dict, Quality, ItemDef, HeroDef


class Item:

    def __init__(self, item_def : ItemDef, quality : Quality):
        if item_def is None:
            raise TypeError("Item definition cannot be None")
        self.item_def = item_def
        self.quality = quality

    @classmethod
    def new(cls, name, quality):
        item_def = items_dict[name]
        return cls(item_def, quality)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(["{}={}".format(k, v) for k, v in vars(self).items()]))

    def break_chance(self, hero):
        if not hero.can_equip(self):
            return -1
        level_difference = abs(hero.level - self.item_def.level)
        affinity_modifier = hero.affinity(self)
        base_break_chance = 1.0 - (1.0 - 0.03 * level_difference - affinity_modifier)**0.85
        break_chance = self.quality.modifier() * max(base_break_chance, 0.03)
        return break_chance if break_chance >= 0.005 else 0.0


class Hero:

    def __init__(self, hero_def : HeroDef, level):
        if hero_def is None:
            raise TypeError("Hero definition cannot be None")
        if level > hero_def.lmax or level < 1:
            raise ValueError("Level {} outside of hero '{}' range (1, {})".format(level, hero_def.name, hero_def.lmax))
        self.hero_def = hero_def
        self.level = level

    @classmethod
    def new(cls, name, level):
        hero_def = heroes_dict[name]
        return cls(hero_def, level)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(["{}={}".format(k, v) for k, v in vars(self).items()]))

    def can_equip(self, item):
        return self.hero_def.can_equip(item.item_def)

    def affinity(self, item):
        return self.hero_def.affinity(item.item_def)


if __name__ == '__main__':
    mojian = Hero.new('Mojian', 40)
    boots = Item.new("King's Boots", Quality.legendary)
    seal = Item.new("Twilight Seal", Quality.flawless)
    ring = Item.new("Undead Ring", Quality.legendary)
    print(boots.break_chance(mojian))
    print(seal.break_chance(mojian))
    print(ring.break_chance(mojian))
