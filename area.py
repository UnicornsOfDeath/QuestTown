class Area:
    def __init__(self, name, enemyStrength, enemyGold, enemyXP):
        self.name = name
        self.enemyStrength = enemyStrength
        self.enemyGold = enemyGold
        self.enemyXP = enemyXP

        # Counter for how many times area used
        self.usedCounter = 0