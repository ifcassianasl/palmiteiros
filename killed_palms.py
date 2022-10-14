import random

def killed_palms(row, column, map_of_palm, death_probability, densities):
  death = 0
  for x in range(row):
    for y in range(column):
      level = map_of_palm[x][y] 
      if(level > 0):
        if random.random() <= death_probability:
          map_of_palm[x][y] = 0
          death += 1      

  densities['death'].append(death)

  return map_of_palm, densities