idade = int(input("Qual a idade? "))

if idade <= 12 :
  print("Criança")

if idade >= 12 :
  if idade <= 17 :
    print("Adolescente")
if idade > 17 :
  print("Adulto")
