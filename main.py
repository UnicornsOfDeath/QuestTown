from adventurer import Adventurer


def main():
    turnsPerDay = 5
    totalNumberOfDays = 30
    day = 1
    turn = 1
    adventurers = []
    adventurersPerTurn = []

    # Add some adventurers
    adventurers.append(Adventurer("Crono"))
    adventurers.append(Adventurer("Red"))

    while day <= totalNumberOfDays:
        print "Day:", day, ", Turn:", turn
        print "The adventurers are:", adventurers
        for a in adventurers:
            a.update()
        adventurers = [a for a in adventurers if a.alive]
        adventurersPerTurn.append(len(adventurers))
        turn += 1
        if turn > turnsPerDay:
            turn = 1
            day += 1
            # Add more adventurers
            adventurers.append(Adventurer("Fred" + str(day) + str(turn)))

    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
    import pprint
    pprint.pprint(list(chunks(adventurersPerTurn, turnsPerDay)))



if __name__ == "__main__":
    main()