from adventurer import Adventurer


def main():
    turn = 0
    adventurers = []

    # Add some adventurers
    adventurers.append(Adventurer("Crono"))
    adventurers.append(Adventurer("Red"))

    while True:
        print "It is turn", turn
        print "The adventurers are:", adventurers
        raw_input("Press enter to go to next turn")
        turn += 1


if __name__ == "__main__":
    main()