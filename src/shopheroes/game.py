from shopheroes.hero import Hero

heroes_list = [
    Hero.new('Azula', 42),
    Hero.new('Edward', 40),
    Hero.new('Mojian', 40),
    Hero.new('Francesca', 40),
    Hero.new('Oneira', 39),
    Hero.new('Darthos', 39),
    Hero.new('Nya', 39),
    Hero.new('Louca', 38),
    Hero.new('Kuro Shobi', 38),
    Hero.new('Alicia', 38),
    Hero.new('Kurul', 38),
    Hero.new('Fiora', 38),
    Hero.new('Odette', 38),
    Hero.new('Irene', 38),
    Hero.new('Mila', 38),
    Hero.new('Lancaster', 38),
    Hero.new('Minh', 38),
    Hero.new('Clovis', 37),
    Hero.new('Gauvin', 37),
    Hero.new('Albert', 37),
    Hero.new('Palash', 37),
    Hero.new('Theor', 35),
    Hero.new('Garreth', 35),
    Hero.new('Karal', 30),
    Hero.new('Melina', 30)
]

heroes = {hero.hero_def.name: hero for hero in heroes_list}
