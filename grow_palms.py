import random

def grow_palms(row, column, map_of_palm):
  avoid_list = []
  for x in range(row):
    for y in range(column):
      level = map_of_palm[x][y]
      if (level > 0 and level < 5 and [x, y] not in avoid_list) :
        map_of_palm[x][y] = level + 1
      if random.randint(0, 1) <= 0.3:
        if level == 5:
          near_neibor = []
          if y-1 >= 0 and map_of_palm[x][y-1] == 0: 
            near_neibor.append([x, y-1])
          if y+1 <= (column - 1) and map_of_palm[x][y+1] == 0: 
            near_neibor.append([x, y+1])
          if x-1 >= 0 and map_of_palm[x-1][y] == 0: 
            near_neibor.append([x-1, y])
          if x+1 <= (row - 1) and map_of_palm[x+1][y] == 0: 
            near_neibor.append([x+1, y])

          if len(near_neibor) > 0:
            new_plant = near_neibor[random.randint(0, len(near_neibor) - 1)]
            map_of_palm[new_plant[0]][new_plant[1]] = 1
            avoid_list.append([new_plant[0], new_plant[1]])
      


  return map_of_palm

