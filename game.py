"""
Class that defines the I/O methods for starting and running the Game of Life.
To start game:
    $ python game.py 
You will be prompted to provide the size of the board, then can start playing!
"""

import board as b
import sys

class game(object):
    """ Constructor for the game class.  Makes a simple game with a board """
    def __init__(self):
        # Is putting more than assignments in the constructor bad practice?
        # I couldn't think of better way to do it...
        self.game_size = input("What size would you like to play? >> ")
        self.board = b.board(self.game_size)

    def play(self):
        """
        Method that will allow you to play the game! 
        By default, the board will be shown at the end of the loop.  
        Use update mode for rapid updating
        """
        update_mode = False
        self.board.show()

        while True:
            std_show = True
            action = raw_input("> ")

            # TODO: Change this to a switch statement, probably easier


            if "set" in action:
                a = action.split()
                self.board.set(int(a[1]), int(a[2]))
            if "unset" in action:
                a = action.split()
                self.board.unset(int(a[1]), int(a[2]))

            elif action == "update" or action == "u":
                self.board.update()
            elif action == "coordinates":
                self.board.show_with_coords()
                std_show = False
            elif action == "update mode on":
                update_mode = True
            elif action == "update mode off":
                update_mode = False
            elif action == "quit":
                sys.exit("Thanks for playing!")

            if(std_show):
                self.board.show()
            if(update_mode):
                self.board.update()
g = game()
g.play()