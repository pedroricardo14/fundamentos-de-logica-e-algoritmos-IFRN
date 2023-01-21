"""6) Escreva um programa que pergunta o valor de depósito inicial para uma poupança, e a taxa de
rendimento mensal. Apresente o saldo dos próximos 24 meses, considerando o rendimento sobre
o saldo atual de cada mês."""

valor = float(input("Depósito inicial: "))
rend = float(input("Rendimento: "))

cont = 1  # inicalização
while cont <= 24 :    # teste lógico
  valor = valor + (rend/100 * valor)
  print(f"Mês {cont} = R$ {valor:.2f}")
  
  cont = cont + 1    # incremento
