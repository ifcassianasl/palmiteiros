# migrar para classes
from fill_palm_map import fill_palm_map
from grow_palms import grow_palms
from killed_palms import killed_palms
import numpy as np

row = int(input('rows: '))
column = int(input('columns: '))
density = int(input('Density (%): '))
death_probability = int(input('Probabilidade de Mortes (%): '))/100
birth_probability = 1 - death_probability
#complementares mortes + nascimento = 1
map_of_palm = np.zeros((row, column), dtype=int)
palms = int(map_of_palm.size * (density / 100))
dead_palms = 0
map_of_palm = fill_palm_map(map_of_palm, palms, row, column)

print('filled map')
print(map_of_palm, end="\n\n")

# Calcular a densidade de cada estágio e total para cada tempo
# Numero total de mortes e nascimentos de cada estágio e total
# Rodar n número de amostras para as mesmas condições iniciais

densities = {
  'birth': [], 
  'death': [],
  'total': [],
}

def calculate_density():
  total = 0
  for x in range(row):
    for y in range(column):
      if map_of_palm[x][y] != 0:
        total += 1
  density = (total * 100)/map_of_palm.size
  densities['total'].append(density)


for i in range(15):
  map_of_palm, densities = grow_palms(row, column, map_of_palm,
birth_probability, densities)
  map_of_palm, densities = killed_palms(row, column, map_of_palm, death_probability, densities)
  calculate_density()
  print('Nascimentos', densities['birth'][-1]) 
  print('Mortes', densities['death'][-1]) 
  print('Densidade', densities['total'][-1]) 
  print(map_of_palm, end="\n\n") 
