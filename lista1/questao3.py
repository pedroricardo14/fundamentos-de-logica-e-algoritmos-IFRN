"""3) Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
Apresentar os valores trocados"""

a = input("Valor de A: ")
b = input("Valor de B: ")

#trocando
c = a      # c é variável auxiliar
a = b
b = c          # a, b = b,a   # poderia ser assim também

print(f"Novo valor de A: {a}")
print(f"Novo valor de B: {b}")
