import random

def fill_palm_map(map_of_palm, palms, row, column):
  for n in range(palms):
    s_row = random.randint(0, row - 1)
    s_column = random.randint(0, column - 1)
    level = random.randint(1, 5)
    map_of_palm[s_row][s_column] = level
  return map_of_palm
