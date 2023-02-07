"""
import random 
qtd = int(input("Quantos jogos deseja fazer? "))
for jogo in range(qtd):
  print("\n===PALPITE===")
  for numero in range(6):
    print(random.randint(1,60), end=" - ")"""

# USANDO SAMPLE

import random 
qtd = int(input("Quantos jogos deseja fazer? "))
for jogo in range(qtd):
  print(random.sample(range(1,61), 6))
