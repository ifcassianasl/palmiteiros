# migrar para classes
from fill_palm_map import fill_palm_map
from grow_palms import grow_palms
from killed_palms import killed_palms
import random
import numpy as np

row = int(input('rows: '))
column = int(input('columns: '))
density = int(input('Density (%): '))
map_of_palm = np.zeros((row, column), dtype=int)
palms = int(map_of_palm.size * (density / 100))
dead_palms = 0
map_of_palm = fill_palm_map(map_of_palm, palms, row, column)

print('filled map')
print(map_of_palm, end="\n\n")

for i in range(5):
  grow_palms(row, column, map_of_palm)
  killed_palms(row, column, map_of_palm)
  print(map_of_palm, end="\n\n") 
