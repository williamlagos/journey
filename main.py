"""
This module contains the implementation of a simple text-based adventure game.

Classes:
    GameState: A class to represent the state of the game.
    AdventureGame: A class to manage the game context and flow.

Functions:
    start_adventure(state): Starts the game by presenting the player with a choice of paths.

Usage:
    Run this module as a script to start the adventure game.
"""

from tree import Node


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


class AdventureGame:
    """
    A class to manage the game context and flow.

    Attributes
    ----------
    state : GameState
        The current state of the game.
    root : Node
        The root node of the decision tree.

    Methods
    -------
    __init__():
        Initializes the AdventureGame with a new GameState and decision tree.
    start():
        Starts the adventure game by presenting the player with a choice of paths.
    """

    def __init__(self):
        self.state = GameState()
        self.root = Node("start")
        self.build_decision_tree()

    def build_decision_tree(self):
        left = Node("left_path")
        right = Node("right_path")
        straight = Node("straight_path")
        rest = Node("rest")

        self.root.left = left
        self.root.right = right
        left.left = straight
        left.right = rest
        right.left = rest
        right.right = straight

    def start(self):
        print("""
            Welcome to the Adventure Game!
            You find yourself in a dark forest with paths leading in different directions.
            Choose your path:
            1. Take the left path
            2. Take the right path
            3. Go straight ahead
            4. Sit and rest
        """)

        current_node = self.root
        while current_node:
            try:
                choice = int(input("What do you want to do? (1/2/3/4): "))
                if choice == 1:
                    current_node = current_node.left
                elif choice == 2:
                    current_node = current_node.right
                elif choice == 3:
                    current_node = current_node.left.left
                elif choice == 4:
                    current_node = current_node.left.right
                else:
                    print("Please choose a valid option (1/2/3/4).")
                    continue

                if current_node:
                    self.execute_action(current_node.data)
                else:
                    print("End of path.")
                    break
            except ValueError:
                print("Please enter a valid number.")

    def execute_action(self, action):
        if action == "left_path":
            self.left_path()
        elif action == "right_path":
            self.right_path()
        elif action == "straight_path":
            self.straight_path()
        elif action == "rest":
            self.rest()

    def left_path(self):
        print(f"""
            You take the left path and encounter a wild animal! 
            Your health is {self.state.health} and your inventory contains: {self.state.inventory}
        """)
        # ...additional code for left path...

    def right_path(self):
        print(f"""
            You take the right path and find a hidden treasure! 
            Your health is {self.state.health} and your inventory contains: {self.state.inventory}
        """)
        # ...additional code for right path...

    def straight_path(self):
        print(f"""
            You go straight ahead and fall into a trap! 
            Your health is {self.state.health} and your inventory contains: {self.state.inventory}
        """)
        # ...additional code for straight path...

    def rest(self):
        print(f"""
            You sit and rest for a while, regaining your strength. 
            Your health is {self.state.health} and your inventory contains: {self.state.inventory}
        """)
        # ...additional code for resting...


if __name__ == "__main__":
    game = AdventureGame()
    game.start()
