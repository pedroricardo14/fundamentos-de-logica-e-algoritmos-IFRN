"""6) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
quantidade de kWh consumidas e o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
"""

consumo = float(input("Consumo? "))
inst = input("Instalação? (R/C/I) ")

if inst == "R" :
  if consumo <= 500 :
    print(f"Total: R$ {consumo*0.40}")
  else :
    print(f"Total: R$ {consumo*0.65}")
    
elif inst == "C" :
  if consumo <= 1000 :
    print(f"Total: R$ {consumo*0.55}")
  else :
    print(f"Total: R$ {consumo*0.60}")

elif inst == "I" :
  if consumo <= 5000 :
    print(f"Total: R$ {consumo*0.55}")
  else :
    print(f"Total: R$ {consumo*0.60}")

else :
  print("Tipo de instalação inválido.")
