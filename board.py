"""
Class that
defines board that will be used used for
the Game of Life. 

Includes all methods to update, show, and change state of board.
"""

import sys
import copy

class board(object):
    """
    Constructor for the board.  Takes a simple parameter: size.
    Size determines the size of the board.  Board will be a square of this size
    """
    def __init__(self, size):
        self.size = size
        self.b = []
        for i in range(0, size):
            self.b.append([])
        for y in range(0, size):
          for x in range(0, size):
            self.b[x].append('.')

  def show(self):
      """
      Shows board by printing to terminal 
      Invoked automatically or with 'show' command ingame
      """
      for y in range(0, self.size):
          for x in range(0, self.size):
              sys.stdout.write(self.b[x][y] + ' ')
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
          elif y >=10:
              sys.stdout.write(str(y))

          for x in range(0, self.size):
              sys.stdout.write(self.b[x][y] + ' ')
          sys.stdout.write('\n')

  def set(self, x, y):
      """ Set a space on the board.  Invoked with 'set' ingame """
      try:
          self.b[x][y] = '#'
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
                  if self.b[x][y] == '.' and living == SURVIVAL:
                      buf[x][y] = '#' 

                  elif self.b[x][y] == '#':
                      if living > OVERPOP or living < UNDERPOP:
                          buf[x][y] = '.'
          self.b = buf

  def living_neighbors(self, x, y):
      """
      Gets living neighbors for a particular cell (ie: cells with value '#').
      """

      # There maybe a simpler way to implement this, it turned out this way
      # was easier than adding a padding of invisible empty cells around the board
      live = 0

      try:
        if self.b[x+1][y] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x][y+1] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x+1][y+1] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x-1][y] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x][y-1] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x-1][y-1] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x-1][y+1] == '#':
            live += 1
      except: 
        pass

      try:
        if self.b[x+1][y-1] == '#':
            live += 1
      except: 
        pass

      return live
