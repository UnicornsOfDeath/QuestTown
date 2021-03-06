#!/usr/bin/env python

from adventurer import Adventurer
from building import *
from area import Area
from random import randint


def main():
    turnsPerDay = 5
    totalNumberOfDays = 30
    day = 1
    turn = 1
    adventurers = []
    adventurersPerTurn = []
    # List of adventurer levels at the end of each day
    adventurerLevelsDay = []
    areas = {}
    buildings = []

    townLevel = 1
    townXP = 0
    townLastLevelXP = 0
    townXPForNextLevel = 1000
    # XP to level up to next, as multiplier
    TOWN_LEVEL_UP_XP_GROWTH_FACTOR = 1.5

    # Add some areas
    def addArea(area):
        areas[area.name] = area
    addArea(Area("Field", 15))
    #addArea(Area("Swamp", 5))
    #addArea(Area("Mountain", 10))

    # Add some adventurers
    adventurers.append(Adventurer("Crono", 1))
    adventurers.append(Adventurer("Red", 1))

    buildings.append(Shop("Ye Old Weapon Shop"))
    buildings.append(Inn("Le Pube"))
    buildings.append(Tavern("We won't watch you sleep"))

    while day <= totalNumberOfDays:
        #print "Day:", day, ", Turn:", turn
        #print "The Buildings are:", buildings
        #print "The adventurers are:", adventurers
        for a in adventurers:
            a.update(areas)
        adventurers = [a for a in adventurers if a.alive]
        adventurersPerTurn.append(len(adventurers))
        turn += 1
        # Town gains xp for every adventurer
        for a in adventurers:
            townXP += a.level * 10
            if townXP > townLastLevelXP + townXPForNextLevel:
                townLevel += 1
                townLastLevelXP += townXPForNextLevel
                townXPForNextLevel *= TOWN_LEVEL_UP_XP_GROWTH_FACTOR
                #print 'Town leveled up to', townLevel
        if turn > turnsPerDay:
            turn = 1
            day += 1
            # Summarise levels
            adventurerLevelsDay.append([a.level for a in adventurers])
            # Add more adventurers
            # Adventurer level depends on town level
            level = randint(1, townLevel)
            adventurers.append(Adventurer("Fred" + str(day) + str(turn),
                                          level))

    """
    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"
    def chunks(l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
    import pprint
    pprint.pprint(list(chunks(adventurersPerTurn, turnsPerDay)))

    print 'Adventurer levels'
    for levelsDay in adventurerLevelsDay:
        if len(levelsDay) == 0:
            print '0'
        else:
            levelCounts = []
            for level in range(1, max(levelsDay) + 1):
                levelCounts.append(str(levelsDay.count(level)))
            print ', '.join(levelCounts)

    print 'Area counters'
    for name, area in areas.iteritems():
        print name, area.usedCounter
    """

    #print 'Town is at level', townLevel
    #print 'Number of adventurers', len(adventurers)
    #print 'Average adventurer level',\
    #    sum([a.level for a in adventurers]) * 1.0 / len(adventurers)
    print townLevel, len(adventurers),\
        sum([a.level for a in adventurers]) * 1.0 / len(adventurers)


if __name__ == "__main__":
    main()