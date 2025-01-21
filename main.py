import random


class GameState:
    def __init__(self):
        self.health = 100
        self.inventory = []


def start_adventure(state):
    print("""
        Welcome to the Adventure Game!
        You find yourself in a dark forest with paths leading in different directions.
        Choose your path:
        1. Take the left path
        2. Take the right path
        3. Go straight ahead
        4. Sit and rest
    """)

    while True:
        try:
            choice = int(input("What do you want to do? (1/2/3/4): "))
            if choice == 1:
                left_path(state)
                break
            elif choice == 2:
                right_path(state)
                break
            elif choice == 3:
                straight_path(state)
                break
            elif choice == 4:
                rest(state)
                break
            else:
                print("Please choose a valid option (1/2/3/4).")
        except ValueError:
            print("Please enter a valid number.")


def left_path(state):
    print("You take the left path and encounter a wild animal!")
    # ...additional code for left path...


def right_path(state):
    print("You take the right path and find a hidden treasure!")
    # ...additional code for right path...


def straight_path(state):
    print("You go straight ahead and fall into a trap!")
    # ...additional code for straight path...


def rest(state):
    print("You sit and rest for a while, regaining your strength.")
    # ...additional code for resting...


if __name__ == "__main__":
    state = GameState()
    start_adventure(state)
