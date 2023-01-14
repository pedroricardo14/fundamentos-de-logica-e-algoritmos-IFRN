#3) Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente

a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Valor C: "))

"""if (a < b) and (a < c) and (b < c) :
  print(a, b, c)
elif (a < b) and (a < c) and (c < b) :
  print(a, c ,b)
elif (b < a) and (b< c) and  (a < c) :
  print(b, a, c)
elif (b < a) and (b < c) and (c < a) :
  print(b, c, a)
elif (c < a ) and (c < b) and (a < b) :
  print(c, a, b)
else :
  print(c, b, a)"""

#Esses são códigos diferentes, mas fazem a mesma coisa. O segundo jeito(que está abaixo) é mais fácil.

lista = [a, b, c]
print(sorted(lista))
