contador = 1
soma = 0
while contador <= 5:
  numero = int(input("Digite: "))
  soma = soma + numero
  if contador == 5:
    break
  contador = contador +1
else:
  print(f"Total = {soma}")
