"""11) Faça um programa que leia a idade de um atleta e informa a qual categoria ele pertence:
Até 8 anos Até 11 anos Até 14 anos Até 17 anos 18 ou mais
pré-mirim mirim infantil juvenil adulto"""

idade = float(input("Idade? "))

if idade <= 8 :
  print("PRÉ-MIRIM")
elif idade <= 11 :
  print("MIRIM")
elif idade <= 14 :
  print("INFANTIL")
elif idade <= 17 :
  print("JUVENIL")
else :
  print("ADULTO")
