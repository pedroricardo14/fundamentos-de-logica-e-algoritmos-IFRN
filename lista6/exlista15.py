# a ordenação de sub-listas é feita pela posição 0 (zero)

prod1 = ["nescau", 7.49]
prod2 = ["feijão", 5.85]
prod3 = ["arroz", 4.75]
prod4 = ["detergente", 1.98]

compras = [prod1, prod2, prod3, prod4]
print(compras)

compras.sort()  #ordena pelo nome do produto
print(compras)

compras.sort(key=lambda x: x[1])    #ordenar por outra coluna
print(compras)
