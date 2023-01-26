frutas = ["laranja", "banana", "manga", "uva", "melancia", "pêra", "caju", "pitaia"]

pesquisa = input("Qual fruta você gosta? ")

if pesquisa in frutas :
  print("Eu vendo essa fruta. Quer comprar? ")
  print(f"Está na prateleira {frutas.index(pesquisa)}")
else :
  print("Essa fruta eu não tenho.")
