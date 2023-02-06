# 1. Crie um programa que use um laço for para solicitar a digitação do nome de 5 alunos. Após a digitação, exiba a lista.  
alunos = []

for x in range(5):
  nome = input("Digite o nome do aluno: ")
  alunos.append(nome)

#print(alunos)          #Ou então
for nome in alunos:
  print(nome)
