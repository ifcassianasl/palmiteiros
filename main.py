# migrar para classes
from fill_palm_map import fill_palm_map
from grow_palms import grow_palms
from killed_palms import killed_palms
import numpy as np

row = int(input('rows: '))
column = int(input('columns: '))
density = int(input('Density (%): '))
morte = int(input('Probabilidade (%): '))
nascimento = 1 - morte/100
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

# quem você é, de onde, o que está fazendo
# bolsista de tal instituição
# Contextualização biologica do processo
# Objetivo: criar uma modelagem para representar isso
# caracteristicas 
# modelo criado em python e etc
# explicar o que é um passo de tempo
# explicar nascimento numa determinada probabilidade por vizinhança
# explicar morte do palmiteiro, sem motivo determinado, com uma determinada probabilidade
# colocar quadros da evoluação do mapa
# colocar diferentes situações
  # probabilidade de morte = 0 nascimento = 0 -> apenas envelhecem, n nasce nem morre
  # probabilidade de morte = 0 nascimento = 100% -> sempre nasce 
  # probabilidade de estados inermediarios considerando (morte + nascimento = 1)
    # p de nascimento alta 
    # p de morte alta 
# considerações finais
  # Fazer a evolução temporal para geração de dados
  # considerar o macaco prego como agente movel pela rede que mata os palmiteiros adultos com uma determinada probabilidade
# Importância: verificar mecanismos de conservação e manejo a especie
# 10 min

for i in range(15):
  grow_palms(row, column, map_of_palm)
  killed_palms(row, column, map_of_palm)
  print(map_of_palm, end="\n\n") 
