"""1) Ler quatro notas de um aluno, calcular a média aritmética e imprimir a média e uma mensagem dizendo que
o aluno foi aprovado, se a média for maior ou igual a 6, ou reprovado para uma nota abaixo de 6.
"""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
media = (n1+n2+n3+n4)/4
if media >= 6 :
  print("Aprovado.")
else :
  print("Reprovado.")
  
