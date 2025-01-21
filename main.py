"""
This module contains the implementation of a simple text-based adventure game.

Classes:
    GameState: A class to represent the state of the game.

Functions:
    start_adventure(state): Starts the game by presenting the player with a choice of paths.
    left_path(state): Handles the scenario when the player chooses the left path.
    right_path(state): Handles the scenario when the player chooses the right path.
    straight_path(state): Handles the scenario when the player chooses to go straight ahead.
    rest(state): Handles the scenario when the player chooses to sit and rest.

Usage:
    Run this module as a script to start the adventure game.
"""


class GameState:
    """
    A class to represent the state of the game.

    Attributes
    ----------
    health : int
        The health of the player.
    inventory : list
        The inventory of the player.

    Methods
    -------
    __init__():
        Initializes the GameState with default values.
    """

    def __init__(self):
        self.health = 100
        self.inventory = []


def start_adventure(state):
    """
    Starts the adventure game by presenting the player with a choice of paths.

    Args:
        state (dict): A dictionary representing the current state of the game.

    The player can choose from the following options:

    The function will call the corresponding function based on the player's choice:
        - left_path(state) for option 1
        - right_path(state) for option 2
        - straight_path(state) for option 3
        - rest(state) for option 4

    If the player enters an invalid option, they will be prompted to try again.
    """
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
    """
    Simulates the scenario when the user takes the left path in the journey.

    Args:
        state (GameState): An instance representing the current state of the journey.

    Returns:
        None
    """
    print(f"""
        You take the left path and encounter a wild animal! 
        Your health is {state.health} and your inventory contains: {state.inventory}
    """)
    # ...additional code for left path...


def right_path(state):
    """
    Simulates taking the right path in a journey and prints a message indicating 
    that a hidden treasure has been found.

    Args:
        state (GameState): An instance representing the current state of the journey.
    """
    print(f""""
        You take the right path and find a hidden treasure! 
        Your health is {state.health} and your inventory contains: {state.inventory}
    """)
    # ...additional code for right path...


def straight_path(state):
    """
    Simulates the action of going straight ahead in the game.

    Args:
        state (GameState): The current state of the game.

    Returns:
        None
    """
    print(f""""
        You go straight ahead and fall into a trap! 
        Your health is {state.health} and your inventory contains: {state.inventory}
    """)
    # ...additional code for straight path...


def rest(state):
    """
    Simulates the action of resting, allowing the character to regain strength.

    Parameters:
    state (object): The current state of the character or game.

    Returns:
    None
    """
    print(f""""
        You sit and rest for a while, regaining your strength. 
        Your health is {state.health} and your inventory contains: {state.inventory}
    """)
    # ...additional code for resting...


if __name__ == "__main__":
    game_state = GameState()
    start_adventure(game_state)
