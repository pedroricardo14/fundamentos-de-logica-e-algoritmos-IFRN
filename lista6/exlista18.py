# criar a cópia de uma lista
lista = ["ana", "bia", "clara"]
nomes = lista.copy()  # sem o copy, as duas palavras apontam pra mesma lista.
nomes[1] = "joao"
print(lista)
print(nomes)
