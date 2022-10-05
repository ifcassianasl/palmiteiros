import random

def killed_palms(row, column, map_of_palm):
  for x in range(row):
    for y in range(column):
      level = map_of_palm[x][y] 
      if random.randint(0, 1) <= 0.3:
        if (level > 0 and level < 5) :
            map_of_palm[x][y] = 0
            print([x, y], "Morreu")      

  return map_of_palm