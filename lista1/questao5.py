"""5) Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do
percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS).
"""
salario = float(input("Salario atual: "))
reajuste = float(input("Reajuste (%): "))
novo = salario + (salario*reajuste/100)
print(f"Novo salário: {novo:.2f}")
