class Adventurer:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.strength = 10
        self.money = 100
        self.xp = 0
        self.level = 1
        self.equipment = []
        self.happiness = 50

    def __repr__(self):
        return '{name} lvl({level}) str({strength}) ${money} xp({xp})'.format(
            **self.__dict__)