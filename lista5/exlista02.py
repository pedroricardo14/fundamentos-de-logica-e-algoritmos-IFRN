cidades = []  #lista vazia

repet = "sim"
while repet == "sim":
    cid = input("Qual cidade você gostaria de visitar? ")
    cidades.append(cid)
    repet = input("Adicionar outro? (sim/nao) ")
else :
  print(f"As cidades digitadas foram: {cidades}")

