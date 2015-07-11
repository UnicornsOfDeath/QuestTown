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
        inp = raw_input("Press enter to go to next turn")
        print inp
        turn += 1
        if turn > turnsPerDay:
            turn = 1
            day += 1
            # Add more adventurers
            adventurers.append(Adventurer("Fred" + str(day) + str(turn)))
        adventurersPerTurn.append(len(adventurers))

    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"
    print adventurersPerTurn



if __name__ == "__main__":
    main()