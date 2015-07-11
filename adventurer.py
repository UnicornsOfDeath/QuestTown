from random import randint


LEVEL_UP_XP = 100
LEVEL_UP_STRENGTH = 2
LEVEL_UP_XP_GROWTH_FACTOR = 1.5


class Adventurer:
    def __init__(self, name, level, areas):
        self.name = name
        self.strength = 10
        self.money = 100
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
        self.lives = 3
        # How much this adventurer likes going to areas
        self.areaLikes = {}
        for area in areas:
            self.areaLikes[area] = 5

    def __repr__(self):
        return '{name}\tlvl({level})\tstr({strength})\t${money}\txp({xp})'.format(
            **self.__dict__)

    def update(self, areas):
        choice = randint(0, 9)
        if 0 <= choice <= 5:
            print self.name, 'wants to fight!'
            # Select a random area based on likes
            likeSum = sum([self.areaLikes[area] for area in self.areaLikes])
            choice = randint(0, likeSum)
            choiceCounter = 0
            for area in self.areaLikes:
                if choiceCounter <= choice < choiceCounter + self.areaLikes[area]:
                    self.fight(areas[area])
                choiceCounter += self.areaLikes[area]
        else:
            print self.name, 'taking a break'

        # Reversion around mean for likes
        for area in self.areaLikes:
            if self.areaLikes[area] < 5:
                self.areaLikes[area] += 1
            elif self.areaLikes[area] > 5:
                self.areaLikes[area] -= 1
        print self.name, 'likes areas', self.areaLikes

    def fight(self, area):
        if randint(0, 20) + self.strength < randint(0, 20) + area.enemyStrength:
            print self.name, 'fought enemy and lost!'
            self.lives -= 1
            # Really don't like this area
            self.areaLikes[area.name] -= 5
            if self.lives == 0:
                print self.name, 'died!'
                self.alive = False
        else:
            print self.name, 'fought enemy and won!'
            self.money += area.enemyGold
            self.addXP(area.enemyXP)
            # Love this area
            self.areaLikes[area.name] += 3

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