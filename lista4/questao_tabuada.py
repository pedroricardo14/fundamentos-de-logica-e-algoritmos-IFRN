"""1) Crie um programa que imprime a tabuada de um número digitado pelo usuário. Ex. Usuário
digitou "2", o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ..."""

tabuada= int(input("Tabuada? "))
numero = 1
while numero <= 10 :
  print(f"{tabuada} x {numero} = {tabuada*numero}")
  numero = numero + 1
  
