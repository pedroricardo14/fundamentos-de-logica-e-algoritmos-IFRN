"""9) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos
impostos, ambos aplicados ao custo de fábrica. Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos
de 45%, prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao consumidor."""

fabrica = float(input("Preço de fábrica: "))
distrib = fabrica * 12 / 100
imposto = fabrica * 45 / 100
total = fabrica + distrib + imposto
print(f"Total a pagar: R$ {total:.2f}")
