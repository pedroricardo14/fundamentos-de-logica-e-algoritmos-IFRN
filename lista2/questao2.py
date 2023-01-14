"""2) Modifique o programa anterior para solicitar a nota da recuperação se o aluno ficou abaixo de 6. Calcule a
média final usando a primeira média e a nota da recuperação. O aluno será aprovado se a média final for 5 ou
mais, caso contrário, será reprovado. Mostre a média final e a mensagem."""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
media = (n1+n2+n3+n4)/4
print(f"Média: {media:.1f}")
if media >= 6 :
  print("Aprovado.")
else :
  nr = float(input("Nota Recup.: "))
  mfinal = (media + nr)/2
  
  print(f"Média final: {mfinal:.1f}")
  if mfinal >= 5 :
      print("Aprovado.")
  else:
    print("Reprovado. :'( ")
