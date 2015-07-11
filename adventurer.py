class Adventurer:
    strength = 10
    money = 100
    xp = 0
    level = 1
    equipment = []
    happiness = 50

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name