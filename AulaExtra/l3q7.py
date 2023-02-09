"""7) Escreva um programa que pergunta o valor inicial de uma dívida, a taxa mensal de juros e o valor que será pago a cada mês. Informe o número de meses necessários para quitar a dívida, o total pago e quanto de juros foi pago."""

divida = float(input("Valor da dívida: "))
divida_original = divida       #pra usar no final e calcular quanto pagou de juros
juros = float(input("Taxa de juros:""(Obs: Não use %)"))
mensal = float(input("Pagamento mensal: "))
meses = 0
pago = 0
while divida > 0:
  if divida >= mensal:
    divida = divida - mensal
    pago += mensal
  else:
    pago += divida
    divida = 0
    
  meses += 1                # conta os meses
  divida = divida + (divida * (juros / 100))

print(f"Tempo gasto para pagar a dívida: {meses} meses")
print(f"Total pago: R$ {pago:.2f}")
print(f"Juros pagos: R$ {pago - divida_original:.2f}")
