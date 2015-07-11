from adventurer import Adventurer


def main():
    turnsPerDay = 5
    totalNumberOfDays = 2
    day = 1
    turn = 1
    adventurers = []

    # Add some adventurers
    adventurers.append(Adventurer("Crono"))
    adventurers.append(Adventurer("Red"))

    while day <= totalNumberOfDays:
        print "Day:", day, ", Turn:", turn
        print "The adventurers are:", adventurers
        for a in adventurers:
            a.update()
        adventurers = [a for a in adventurers if a.alive]

        #print "1. Build Building"
        #print "2. Upgrade Building"
        #print "3. Give Quest to Hero"

        inp = raw_input("Press Enter to continue")
        #print inp
        turn += 1
        if turn > turnsPerDay:
            turn = 1
            day += 1
            adventurers.append(Adventurer("Fred" + str(day) + str(turn)))

    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"



if __name__ == "__main__":
    main()