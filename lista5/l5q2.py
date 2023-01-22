"""2. Crie um programa em que o usuário digite 10 valores em uma lista e depois imprima a
lista."""

lista = []
cont=1
while cont<=10:
  valor = input("Digite um valor: ")
  lista.append(valor)
  cont = cont + 1
print(lista)
