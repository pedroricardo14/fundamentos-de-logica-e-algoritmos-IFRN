alunos = ["abel", "bianca", "celino", "diana", "elias", "fernanda", "gabriel", "helenice"]
print(alunos)

pos = int(input("Qual posição quer remover? "))

if pos < len(alunos): 
  alunos.pop(pos)
  print("Removido com sucesso.")
else: 
  print("Posiçã não existe")

print(alunos)
