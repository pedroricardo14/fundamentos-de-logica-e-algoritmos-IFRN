frutas = []    # lista vazia

while True:
  item = input("Digite uma fruta: ")
  frutas.append(item)
  continuar = input("Cadastrar outra? (s/n) ")
  if continuar == "n":
    break

print(frutas)
print(f"{len(frutas)} itens cadastrados.")
