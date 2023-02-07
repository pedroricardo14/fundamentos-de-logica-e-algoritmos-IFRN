"""4. Crie um programa que pergunta quantos alunos participam de uma classe. Use um laço
for para solicitar a digitação do nome e da nota para cada aluno, armazenando tudo em
uma lista. Após a digitação, percorra a lista (usando um laço for) e imprima frases com o
nome, nota e resultado do aluno, de acordo com as regras abaixo.
De 60 a 100 – aprovado.
De 40 a 59 – em recuperação.
Abaixo de 40 – reprovado.
Veja o exemplo de saída:
João tem média 100 e está aprovado.
Maria tem média 50 e está em recuperação.
Carlos tem média 30 e está reprovado."""

qtd = int(input("Quantos alunos? "))
alunos = []
for alu in range(qtd):      # DIGITAÇÃO 
  nome = input("Nome do aluno: ")
  nota = float(input("Nota do aluno: "))
  alunos.append([nome, nota])

for aluno in alunos:    # EXIBIÇÃO 
  if aluno[1] >= 60:  # nota  
    print(f"{aluno[0]} tem média {aluno[1]} e está aprovado.")
  elif aluno[1] >= 40:
    print(f"{aluno[0]} tem média {aluno[1]} e está em recuperação.")
  else:
    print(f"{aluno[0]} tem média {aluno[1]} e está reprovado.")
  

