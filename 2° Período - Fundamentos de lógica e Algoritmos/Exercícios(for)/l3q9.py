"""
9) Elaborar um programa que apresente os valores de conversão de graus para Celsius em fahrenheit, de 10 em 10 graus, iniciando a contagem"""

for c in range(10,101, 10):
  print(f"{c}°C = {(9*c+160)/5}°F")
