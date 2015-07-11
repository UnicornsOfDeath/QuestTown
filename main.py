from adventurer import Adventurer
from area import Area


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

    # Add some areas
    def addArea(area):
        areas[area.name] = area
    addArea(Area("Field", 4, 4, 3))
    addArea(Area("Swamp", 5, 10, 10))
    addArea(Area("Mountain", 6, 20, 30))

    # Add some adventurers
    adventurers.append(Adventurer("Crono", areas))
    adventurers.append(Adventurer("Red", areas))

    while day <= totalNumberOfDays:
        print "Day:", day, ", Turn:", turn
        print "The adventurers are:", adventurers
        for a in adventurers:
            a.update(areas)
        adventurers = [a for a in adventurers if a.alive]
        adventurersPerTurn.append(len(adventurers))
        turn += 1
        if turn > turnsPerDay:
            turn = 1
            day += 1
            # Summarise levels
            adventurerLevelsDay.append([a.level for a in adventurers])
            # Add more adventurers
            adventurers.append(Adventurer("Fred" + str(day) + str(turn),
                                          areas))

    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
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



if __name__ == "__main__":
    main()