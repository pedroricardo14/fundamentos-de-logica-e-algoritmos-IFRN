# 3. Crie um programa que pede ao usuário para digitar uma frase. O programa deve usar um laço for para contar quantos caracteres existem na frase (incluindo espaços e pontuação) e mostrar a quantidade. NÃO use o comando len() para descobrir o tamanho da frase.

frase = input("Digite uma frase: ")
quant = 0
for letra in frase:
  quant = quant + 1
else:
  print(f"Essa frase tem {quant} caracteres.")
