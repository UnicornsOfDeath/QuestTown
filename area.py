class Area:
    def __init__(self, name, enemyStrength):
        self.name = name
        self.enemyStrength = enemyStrength
        self.enemyGold = goldFormula(enemyStrength)
        self.enemyXP = xpFormula(enemyStrength)

        # Counter for how many times area used
        self.usedCounter = 0

def goldFormula(strength):
    return 1.4**strength

def xpFormula(strength):
    return 1.5**strength