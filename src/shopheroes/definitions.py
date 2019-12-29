import jsons


class ItemDef:

    def __init__(self, name, level, klass, power):
        self.name = name
        self.level = int(level)
        self.klass = klass
        self.power = power


class EqDef:

    def __init__(self, klass, type, affinity):
        self.klass = klass
        self.type = type
        self.affinity = affinity


class HeroDef:

    def __init__(self, name, lmax, power_start, power_multi, eq_defs):
        self.name = name
        self.lmax = lmax
        self.power_start = power_start
        self.power_multi = power_multi
        self.eq_defs = eq_defs

