alunos = ["abel", "bianca", "celino", "diana", "elias", "fernanda", "gabriel", "helenice"]
print(alunos)
pesquisa = input("Quem deseja remover? ")

if pesquisa in alunos:
  alunos.remove(pesquisa)        #remover itens da lista
else :
  print("Aluno não encontrado")
print(alunos)

