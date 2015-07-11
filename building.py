class Building:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{name}'.format(
            **self.__dict__)

class Shop(Building):
    def __init__(self, name):
        self.name = name

class Inn(Building):
    def __init__(self, name):
        self.name = name

class Tavern(Building):
    def __init__(self, name):
        self.name = name