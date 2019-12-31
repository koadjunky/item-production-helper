import os.path
from enum import IntEnum
from typing import Dict, List
import jsons

libdir = os.path.dirname(os.path.realpath(__file__))


class Quality(IntEnum):
    base = 0
    good = 1
    great = 2
    flawless = 3
    epic = 4
    legendary = 5
    mythical = 6

    # Library jsons serializes Quality.base as "0". To deserialize, we need following method:
    @classmethod
    def _missing_(cls, value):
        try:
            if int(value) in cls._value2member_map_:
                return cls._value2member_map_[int(value)]
        except:
            raise ValueError("%r is not a valid %s" % (value, cls.__name__))

    def modifier(self):
        return [1, 0.75, 0.5, 0.3, 0.15, 0.05, 0.04][self.value]


class Craft(IntEnum):
    AVAILABLE = 0
    COMMON = 1
    BLUEPRINT = 2
    PREMIUM = 3
    TRADE_WAR = 4

    # Library jsons serializes Availability.AVAILABLE as "0". To deserialize, we need following method:
    @classmethod
    def _missing_(cls, value):
        try:
            if int(value) in cls._value2member_map_:
                return cls._value2member_map_[int(value)]
        except:
            raise ValueError("%r is not a valid %s" % (value, cls.__name__))


class ItemDef:

    def __init__(self, name, level, klass, power : Dict[Quality, int]):
        self.name = name
        self.level = level
        self.klass = klass
        self.craft = Craft.AVAILABLE
        self.power = power

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(["{}={}".format(k, v) for k, v in vars(self).items()]))


class EqDef:

    def __init__(self, klass, type, affinity):
        self.klass = klass
        self.type = type
        self.affinity = affinity

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(["{}={}".format(k, v) for k, v in vars(self).items()]))


class HeroDef:

    def __init__(self, name, lmax, power_start, power_multi, eq_defs : List[EqDef]):
        self.name = name
        self.lmax = lmax
        self.power_start = power_start
        self.power_multi = power_multi
        self.eq_defs = eq_defs

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(["{}={}".format(k, v) for k, v in vars(self).items()]))

    def can_equip(self, item_def : ItemDef):
        for eq_def in self.eq_defs:
            if item_def.klass == eq_def.klass:
                return True
        return False

    def affinity(self, item_def : ItemDef):
        for eq_def in self.eq_defs:
            if item_def.klass == eq_def.klass:
                return eq_def.affinity
        raise ValueError("Item '{}' cannot be equipped by {}".format(item_def.name, self.name))


with open(os.path.join(libdir, 'resources', 'items.json'), "r") as file:
    items_list = jsons.loads(file.read(), List[ItemDef])
items_dict = {item.name: item for item in items_list}

with open(os.path.join(libdir, 'resources', 'heroes.json'), "r") as file:
    heroes_list = jsons.loads(file.read(), List[HeroDef])
heroes_dict = {hero.name: hero for hero in heroes_list}


if __name__ == '__main__':
    import pprint
    pprint.pprint(items_dict)
    pprint.pprint(heroes_dict)
