"""7. Crie um programa que simule um painel eletrônico que organiza uma fila. O programa
exibe um menu com as seguintes opções: 1. Entrar na fila. / 2. Consultar a fila. / 3. Chamar
próximo da fila. Na opção 1, o usuário digita o nome da pessoa que está entrando no final
da fila. Na opção 2, o programa imprime a fila atual e diz *quantas pessoas há na fila*. Na
opção 3, o programa exibe uma mensagem chamando a pessoa da vez e remove seu nome
da fila. Se não houver pessoas na fila, mostre a mensagem "fila vazia"."""

fila = []      # lista vazia
while True:     # laço infinito
  print("===MENU===")
  print("1 - Entrar na fila")
  print("2 - Consultar fila")
  print("3 - Chamar o próximo da fila")
  opcao = int(input("Digite uma opção: "))

  if opcao == 1:
    nome = input("Digite um nome: ")
    fila.append(nome)
    print(f"{nome} entrou na fila.\n")

  if opcao == 2:
    print(f"{fila} \n")

  if opcao == 3:
   if len(fila) == 0:
    print(f"{fila[0]} será atendido agora.")
    fila.pop(0)  # remove a posição indicada da lista
