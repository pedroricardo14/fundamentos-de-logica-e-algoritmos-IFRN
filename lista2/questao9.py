"""9) Uma empresa paga R$ 12,50 por hora trabalhada (até 40 horas) e 18,50 por hora extra. Leia o número de
horas semanais de um funcionário e informe o valor do pagamento da semana.
"""

horas = float(input("Horas? "))

if horas <= 40 :
  print(f"Valor a receber: R$ {horas*12.50}")
else : 
  extras = horas - 40
  print(f"Valor a receber: R$ {40*12.50 + extras*18.50}")
