import sys
import copy

class board(object):
  def __init__(self, size):
      self.size = size
      self.b = []
      for i in range(0, size):
          self.b.append([])
      for y in range(0, size):
        for x in range(0, size):
          self.b[x].append('.')

  def show(self):
      for y in range(0, self.size):
          for x in range(0, self.size):
              sys.stdout.write(self.b[x][y] + ' ')
          sys.stdout.write('\n')

  def show_with_coords(self):
      sys.stdout.write("  ")
      for i in range(0, self.size):
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
      try:
          self.b[x][y] = '#'
      except:
          print "Not a valid set command"
  def unset(self, x, y):
      try:
          self.b[x][y] = '.'
      except:
          print "Not a valid unset command"
  def update(self):
      buf = copy.deepcopy(self.b)
      for y in range(0, self.size):
        for x in range(0, self.size):
          living = self.living_neighbors(x,y)
          if self.b[x][y] == '.' and living == 3 or living == 4:
              buf[x][y] = '#'     
          elif self.b[x][y] == '#':
            if living > 3 or living < 2:
              buf[x][y] = '.'
      self.b = buf

  def living_neighbors(self, x, y):
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
