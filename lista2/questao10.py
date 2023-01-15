"""10) Escreva um programa que o usuário informa o valor do salário e o programa calcula o novo salário de acordo
com as seguintes condições:"""

salario = float(input("Salário? "))

if salario <=1000 :
  print(f"Novo salário: R$ {salario * 1.55}")
elif salario <= 2000 :
  print(f"Novo salário: R$ {salario * 1.10}")
elif salario <= 3000 :
  print(f"Novo salário: R$ {salario * 1.05}")
else : 
  print(f"Novo salário: R$ {salario * 1.025}")
