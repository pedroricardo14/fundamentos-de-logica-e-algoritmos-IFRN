#1. Crie uma sequência de 0 até 14.  
"""print(list(range(15)))"""

#2. Crie uma sequência de 0 até 30.  
"""sequencia = list(range(30 + 1))    # ou 31
print(sequencia)"""  

#3. Crie uma sequência de 1 até 25
"""print(list(range(1, 26)))"""

#4. Crie uma sequência de 5 até 49.
"""numeros = list(range(5, 49 + 1))    # range(5, 50)
print(numeros)"""

#5. Crie uma sequencia com os números pares de 2 até 16.
"""pares = list(range(2, 16 + 1, 2))    #range(2,17,2)
print(pares)"""

"""#6. Crie uma sequência com os números ímpares de 7 até 27.
print(list(range(7, 28, 2)))"""

#7. Crie uma sequência decrescente de 10 até 0.  #range(10,0-1,-1)
"""print(list(range(10, -1, -1)))"""

#8. Crie uma sequência decrescente de 30 até 20.
"""seq = list(range(30,20-1,-1))  #range(30, 19,-1)
print(seq)"""

#9. Crie uma sequência decrescente dos números pares de 50 até 38.
"""print(list(range(50, 38-1, -2)))    #range(50,37,-2)"""

#10. Crie uma sequência decrescente de 99 até 33 que diminui de 3 em 3.
"""numeros = list(range(99,32,-3))
print(numeros)"""

#11. Qual comando gera a sequência: [18, 21, 24, 27, 30]?
"""print(list(range(18,31,3)))"""

#12. Qual comando gera a sequência: [35, 46, 57, 68, 79]?
"""print(list(range(35,80,11)))"""

#13. Qual comando gera a sequência: [77, 70, 63, 56]?
"""print(list(range(77,50,-7)))"""

#14. Qual comando gera a sequência: [400, 300, 200, 100, 0]?
"""print(list(range(400, -1,-100)))"""

#15. Crie um programa que pede ao usuário para digitar: o número inicial de uma
#sequência (menor valor), o número final de uma sequência (maior valor). Imprima
#a sequência desejada.

"""inicial = int(input("Inicio da sequêcia: "))
final = int(input("Final da sequência: "))
print(list(range(inicial, final+1)))"""

#16. Modifique o programa anterior para que ele também possa gerar sequências
#decrescentes. O programa deve identificar automaticamente se é uma sequência crescente ou decrescente. Ex.: Se o usuário digitar 1 e 5, ele vai imprimir: 1, 2, 3, 4, 5. Se o usuário digitar 5 e 1, ele vai imprimir: 5, 4, 3, 2, 1.

"""inicio = int(input("Inicio da sequência: "))
final = int(input("Final da sequência: "))

if inicio < final:
  print(list(range(inicio, final + 1)))  # Crescente
else:
  print(list(range(inicio, final-1, -1)))  # Decrescente"""


#17. Crie um programa que pede ao usuário para digitar: o número inicial de uma
#sequência, o número final de uma sequência, o incremento da sequência. Imprima
#a sequência desejada. Obs.: O programa deve detectar se a sequencia é crescente
#ou decrescente e fazer o incremento (positivo ou negativo) corretamente. Ex.: Se
#o usuário digitar 10 (ini.), 4 (fim), 2 (incr.), o programa deve imprimir: 10, 8, 6, 4,mesmo tendo digitado um incremento positivo.

print("GERADOR DE SEQUÊNCIAS CRES/DECR COM INCREMENTO")

inicio = int(input("Inicio da sequência: "))
final = int(input("Final da sequência: "))
incr = int(input("Incremento da sequência: "))

if incr < 0:        # se for negativo
  incr = incr * -1  # transforma em positivo


if inicio < final:
  print(list(range(inicio, final+1 + incr)))  # Crescente
else:
  print(list(range(inicio, final-1, -incr)))  # Decrescente"""
