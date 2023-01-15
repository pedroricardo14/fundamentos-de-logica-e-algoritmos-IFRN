# Digite o dia da semana
# e o turno o programa
#informa se tem aula
#de algoritmo

dia = input("Dia? ")
turno = input("Turno? ")

if dia == "quinta" and turno == "manhã" :
  print("Tem aula!")
else:
  print("Não tem aula!")



if dia == "quinta" :
  if turno == "manhã" :
    print("Tem aula.")
