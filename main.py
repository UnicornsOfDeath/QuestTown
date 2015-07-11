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
        inp = raw_input("Press enter to go to next turn")
        print inp
        turn += 1
        if (turn > turnsPerDay):
            turn = 1
            day += 1

    print "Shit bro.... Your village is burning, your maidens are raped and your children are murdered"



if __name__ == "__main__":
    main()