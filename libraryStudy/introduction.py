# pensar em um programa que joga uma moeda e gera aleatóriamente se ela vai
# cair cara ou coroa

# existem duas formas que podemos usar para importar funções de bibliotecas
import random # - Importa todas as funções da lib random


#!  from random import choice # - importa apenas a função choice da lib random 

#* coinDown = random.choice([0,1]) 
# ou poderiamos ter
# *coinDown = random.choice(["cara", "coroa"])

# *print(coinDown)

# outro exemplo usando 
# *intrandom = random.randint(1,10) # geramos um número inteiro "random" entre 1 e 10

# *print(intrandom)

import statistics #importamos a biblioteca statistics

mean = statistics.mean([8.9, 10, 5, 8]) # função mean permite que encontremos a média dos valores

print(mean)