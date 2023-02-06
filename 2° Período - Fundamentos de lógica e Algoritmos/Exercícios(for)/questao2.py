# 2. Crie um programa que use um laço for e realize a soma dos números pares de 2 até 20.Exiba o resultado da soma.

soma = 0
for x in range(2, 21, 2):
  soma = soma + x
else:
  print(f"total={soma}")
