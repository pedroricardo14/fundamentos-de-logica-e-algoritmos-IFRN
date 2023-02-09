"""11) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário. **SOLUÇÃO USANDO LISTAS**"""

lista=[]
num = 1
while num >= 0:
  num = int(input("Digite um número positivo: "))
  if num >= 0:
    lista.append(num)
print(f"Maior valor digitado = {max(lista)}")
print(f"Menor vaklor digitado = {min(lista)}")

