"""8) Numa cidade litorânea há lei municipal que permite a produção de 50 Kg de pescados por dia. Sempre que
um pescador chega à praia, um fiscal pesa os peixes e aplica uma multa de R$ 4,00 por cada Kg excedente. Faça
um programa que leia o peso e informe o valor da multa, caso ultrapasse o peso permitido.
"""

peso = float(input("Peso? "))

if peso > 50 :
  print(f"Multa: R$ {(peso-50)*4.00:.2f}")
else :
  print("Sem multa.")
  
