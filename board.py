"""
Class that defines board that will be used used for the Game of Life. 
Includes all methods to update, show, and change state of board.
"""

import sys
import copy
DEAD = 0
LIVE = 1

class board(object):

    def __init__(self, size):
        """
        Constructor for the board.  Takes a simple parameter: size.
        Size determines the size of the board.  Board will be a square of this size
        """
        self.size = size
        # b is main 2D array attribute
        self.b = []
        for i in range(0, size):
            self.b.append([])
        for y in range(0, size):
          for x in range(0, size):
            self.b[x].append(DEAD)

    def show(self):
        """
        Shows board by printing to terminal 
        Invoked automatically or with 'show' command ingame
        """
        for y in range(0, self.size):
            for x in range(0, self.size):
                if self.b[x][y]:
                    sys.stdout.write('#' + ' ')
                elif not self.b[x][y]:
                    sys.stdout.write('.' + ' ')
            sys.stdout.write('\n')

    def show_with_coords(self):
        """ 
        Shows board with coordinates, useful for setting specific coordinates.
        Invoked with 'coordinates' command ingame
        """
        sys.stdout.write("  ")
        for i in range(0, self.size):
            # Keep spacing consistent, include a space for single digits
            if i < 10:
                sys.stdout.write(str(i) + " ")
            elif i >=10:
                sys.stdout.write(str(i))
        sys.stdout.write("\n")

        for y in range(0, self.size):
            if y < 10:
                sys.stdout.write(str(y) + " ")
            elif y >= 10:
                sys.stdout.write(str(y))

            for x in range(0, self.size):
                if self.b[x][y]:
                    sys.stdout.write('#' + ' ')
                elif not self.b[x][y]:
                    sys.stdout.write('.' + ' ')
            sys.stdout.write('\n')

    def set(self, x, y):
        """ Set a space on the board.  Invoked with 'set' ingame """
        try:
            self.b[x][y] = LIVE
        except:
            print "Not a valid set command"

    def unset(self, x, y):
        """ Unset a space on the board. Invoked with 'unset' ingame """
        try:
            self.b[x][y] = '.'
        except:
            print "Not a valid unset command"

    def update(self):
        """
        Main update routine for board.  Will set cells according to ruleset.
        Invoked with 'update' or simple by pressing enter when update mode is on.
        Rules adjustable by adjusting constants below, makes for some fun.
        """

        # TODO: add methods to adjust the ruleset ingame
        OVERPOP = 3
        UNDERPOP = 2
        SURVIVAL = 3

        buf = copy.deepcopy(self.b)
        for y in range(0, self.size):
            for x in range(0, self.size):
                living = self.living_neighbors(x,y)
                if self.b[x][y] == DEAD and living == SURVIVAL:
                    buf[x][y] = LIVE 

                elif self.b[x][y] == LIVE:
                    if living > OVERPOP or living < UNDERPOP:
                        buf[x][y] = DEAD
        self.b = buf

    def living_neighbors(self, x, y):
        """
        Gets living neighbors for a particular cell (ie: cells with value LIVE).
        """

        # There may be a simpler way to implement this, it turned out this way
        # was easier than adding a padding of invisible empty cells around the board
        living = 0

        try:
          if self.b[x+1][y] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x][y+1] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x+1][y+1] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x-1][y] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x][y-1] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x-1][y-1] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x-1][y+1] == LIVE:
              living += 1
        except: 
          pass

        try:
          if self.b[x+1][y-1] == LIVE:
              living += 1
        except: 
          pass

        return living
