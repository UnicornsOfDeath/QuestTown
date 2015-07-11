class Building:
    def __init__(self, name, type):
        self.name = name
        self.type = type


    def __repr__(self):
        return '{name}\t{type}'