dia = input("Dia da semana? ")
diarias = int(input("Quantidade de diárias? "))
hospedes = int(input("Qtd hospedes? "))

if dia == "sexta" and diarias >= 3 and hospedes <= 4 :
  print("Reserva confirmada.")
else :
  print("Falar com a recepção do hotel.")

#o and serve para amenizar o uso do if. O and só funciona quando todas as respostas forem "sim". Quando é sim em uma e não em outra não dá certo pois ele não pula para o else.
