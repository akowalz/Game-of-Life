import board as b
import sys

class game(object):
    def __init__(self):
        self.game_size = input("What size would you like to play? >> ")
        self.board = b.board(self.game_size)

    def play(self):
        update_mode = False
        self.board.show()
        while True:
            std_show = True
            action = raw_input("> ")


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