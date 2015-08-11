from random import randint


LEVEL_UP_XP = 100
LEVEL_UP_STRENGTH = 2
LEVEL_UP_XP_GROWTH_FACTOR = 1.5
LIVES = 3


class Adventurer:
    def __init__(self, name, level):
        self.name = name
        self.strength = 10
        self.money = 100
        self.lives = LIVES
        self.xp = 0
        self.lastLevelXP = 0
        self.xpForNextLevel = LEVEL_UP_XP
        self.level = 1
        for i in range(1, level):
            self.xp += self.xpForNextLevel
            self.levelUp()
        self.equipment = []
        self.happiness = 50
        self.alive = True

    def __repr__(self):
        return '{name}\tlvl({level})\tstr({strength})\t${money}\txp({xp})'.format(
            **self.__dict__)

    def update(self, areas):
        choice = randint(0, 9)
        if 0 <= choice <= 5:
            print self.name, 'wants to fight!'
            # Select a random area based on relative strength
            likes = {}
            likeSum = 0
            for k in areas:
                diff = abs(self.strength - 8 - areas[k].enemyStrength)
                likeAmount = max([0, 20 - diff])
                likes[k] = likeAmount
                likeSum += likeAmount
            choice = randint(0, likeSum)
            choiceCounter = 0
            for k in likes:
                if choiceCounter <= choice < choiceCounter + likes[k]:
                    self.fight(areas[k])
                choiceCounter += likes[k]
        else:
            print self.name, 'taking a break'

    def fight(self, area):
        area.usedCounter += 1
        if randint(0, 20) + self.strength < randint(0, 20) + area.enemyStrength:
            print self.name, 'fought enemy and lost!'
            self.lives -= 1
            if self.lives == 0:
                print self.name, 'died!'
                self.alive = False
        else:
            print self.name, 'fought enemy and won!'
            self.money += area.enemyGold
            self.addXP(area.enemyXP)

    def addXP(self, xp):
        self.xp += xp
        if self.xp > self.lastLevelXP + self.xpForNextLevel:
            self.levelUp()
            print '{name} grew to level {level}!'.format(**self.__dict__)

    def levelUp(self):
        self.level += 1
        self.lastLevelXP += self.xpForNextLevel
        self.xpForNextLevel *= LEVEL_UP_XP_GROWTH_FACTOR
        self.strength += LEVEL_UP_STRENGTH
        self.lives = LIVES