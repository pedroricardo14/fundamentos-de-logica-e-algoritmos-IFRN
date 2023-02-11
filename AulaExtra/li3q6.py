"""6. Crie um programa que sorteie números aleatórios entre 1 e 100. Preencha uma lista com
20 elementos *diferentes*, organize em ordem decrescente e imprima na tela."""

import random 

numeros = []

while len(numeros) < 20 :            # tamanho a lista menor que 20
  sorteio = random.randint(1, 100)     # sorteia o número
  if sorteio in numeros:              # verifica se existe na lista
    continue            # se existe, reinicia o laço
  else:                    # se não existe, arescenta na lista
    numeros.append(sorteio)      #incremeto

else:
  numeros.sort()        # classifica crescente
  numeros.reverse()      # inverte a lista ( para ficar decrescente)
  print(numeros)        # exib a lista
