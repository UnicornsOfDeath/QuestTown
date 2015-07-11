from random import randint


ENEMY_STRENGTH = 5
ENEMY_GOLD = 10
ENEMY_XP = 10
LEVEL_UP_XP = 100
LEVEL_UP_STRENGTH = 2


class Adventurer:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.money = 100
        self.xp = 0
        self.level = 1
        self.equipment = []
        self.happiness = 50
        self.alive = True

    def __repr__(self):
        return '{name}]\tlvl({level})\tstr({strength})\t${money}\txp({xp})'.format(
            **self.__dict__)

    def update(self):
        choice = randint(0, 9)
        if 0 <= choice <= 5:
            print self.name, 'wants to fight!'
            self.fight()
        else:
            print self.name, 'taking a break'

    def fight(self):
        if randint(0, 20) + self.strength < randint(0, 20) + ENEMY_STRENGTH:
            print self.name, 'fought enemy and lost!'
            self.alive = False
        else:
            print self.name, 'fought enemy and won!'
            self.money += ENEMY_GOLD
            self.addXP(ENEMY_XP)

    def addXP(self, xp):
        self.xp += xp
        if self.xp > LEVEL_UP_XP:
            self.level += 1
            print '{name} grew to level {level}!'.format(**self.__dict__)
            self.xp -= LEVEL_UP_XP
            self.strength += LEVEL_UP_STRENGTH