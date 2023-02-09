"""11) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário."""

num = 1    #iniialização
maior = "nenhum"
menor = "nenhum"
while num >= 0:      #teste lógico
  num = int(input("Digite um número positivo: "))    #incremento
  if num >= 0 :
    if maior == "nenhum" and menor == "nenhum":   #primeira digitação
      maior = num
      menor = num
  elif num > maior:
    maior = num 
  elif num < menor:
    menor = num 
    
print(f"Maior valor digitado = {maior}")
print(f"menor valor digitado = {menor}")
