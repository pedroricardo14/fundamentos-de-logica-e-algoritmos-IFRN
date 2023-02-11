"""5. Crie um programa que o usuário digita os dados de duas listas com 3 elementos cada.
Depois crie uma terceira lista com a junção dos elementos das outras duas. Imprima a nova
lista."""


esportes = []
brincadeiras = []

esportes.append(input("Digite um esporte: "))
esportes.append(input("Digite um esporte: "))
esportes.append(input("Digite um esporte: "))

brincadeiras = []
brincadeiras.append(input("Digite uma brincadeira: "))
brincadeiras.append(input("Digite uma brincadeira: "))
brincadeiras.append(input("Digite uma brincadeira: "))

ativ_fisicas = esportes + brincadeiras
print(ativ_fisicas)
