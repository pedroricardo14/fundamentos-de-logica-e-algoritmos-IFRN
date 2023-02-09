"""4. Crie um programa que cadastre os alunos de uma escola. Pergunte ao usuário o nome, o
curso e a série de um aluno. Salve esses 3 dados como uma (sub)lista e depois acrescente
esta (sub)lista em uma lista principal. O programa deve repetir quantas vezes o usuário
desejar. Ao finalizar os cadastros, imprima todos os alunos cadastrados."""

alunos = []
resposta = "s" 
while resposta == "s":
  nome = input("Digite o nome: ")
  curso = input("Digite o curso: ")
  serie = input("Digite a série: ")
  novo = [nome, curso, serie]
  alunos.append(novo)
  resposta = input("Deseja adicionar outro? (s/n) ")
else:
  print(alunos)
