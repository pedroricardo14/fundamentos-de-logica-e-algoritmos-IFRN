clientes = []    # lista vazia

while True:      #laço infinito

  nome = input("Nome do cliente? ")
  fone = input("Telefone do cliente: ")
  contato = [nome,fone]
  clientes.append(contato)
  print("Cadastrado com sucesso.")
  continua = input("Continuar? (s/n) ")
  if continua == "n":
    break    # saída do laço
print(clientes)

  
  
