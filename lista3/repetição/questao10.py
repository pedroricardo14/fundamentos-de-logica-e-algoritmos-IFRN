"""10) Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha, banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor total acumulado da área residencial."""

resposta = "sim"  # valor inicial
area_total = 0
while resposta == "sim":    # teste lógico
  nome = input("Qual o cômodo? ")
  largura = float(input("Largura? "))
  comprimento = float(input("Comprimento? "))
  area = largura * comprimento
  print(f"{nome} tem {area} m²")
  area_total = area_total + area 
  resposta = input("Calcular outro cômodo? ")    # incremento
else: 
  print(f"Área total = {area_total} m².")
  
