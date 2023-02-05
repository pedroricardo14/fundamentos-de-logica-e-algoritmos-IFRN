# 1) Crie um programa que imprime a tabuada de um número digitado pelo usuário. Ex: Usuário digitou "2", o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6...

tabuada = int(input("Qual tabuada desja exibir? "))
for numero in range(1, 11):
  print(f"{tabuada} x {numero} = {tabuada*numero}")
