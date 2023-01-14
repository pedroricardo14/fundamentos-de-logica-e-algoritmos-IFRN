"""7) Informe a altura e o sexo de uma pessoa e calcule o peso ideal, utilizando as seguintes fórmulas: Para homens:
(72*altura)-58. Para mulheres: (62.1*altura)-44.7
"""

altura = float(input("Qual a altura? "))
sexo = input("Sexo (M/F)? ")

if sexo == "M" :
  print(f"Peso ideal: {(72*altura)-58}kg")
else :
  print(f"Peso ideal: {(62.1*altura)-44.7}kg")
