"""8) Digite as notas de um aluno para os 4 bimestres do ano e calcule a sua média ponderada. Os pesos para cada
bimestre são, respectivamente: 2, 3, 4, 6."""

n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))
n4 = float(input("Nota4: "))
media = (n1*2 + n2*3 +n3*4 +n4*6)/15
print(f"Média: {media:.1f}")
