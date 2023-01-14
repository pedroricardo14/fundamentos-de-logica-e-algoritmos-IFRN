"""4) Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando
se o número é par ou ímpar.
"""

num = int(input("Digite um número: "))

resto = num % 2
if resto == 0 :
  print("Esse número é PAR.")
else:
    print("Esse número é IMPAR.")
