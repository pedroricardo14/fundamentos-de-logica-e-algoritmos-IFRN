# Utilizando While
lista = ["Carlos", "Ana", "João", "Lidia"]

"""posicao = 0  #inicial
while posicao < len(lista):    #teste
  print(f"Seja bem vindo, {lista[posicao]}!")
  posicao = posicao + 1   #incremento"""

  #Utilizando o for

"""lista = ["Carlos", "Ana", "João", "Lidia"]
for nome in lista:
   print(f"Seja bem vindo, {nome}!")"""

#Uma string é uma lista de caracteres

"""for letra in "ESCOLA":
  print(letra)"""

#exemplo usando break (finalizar o laço via comando)

"""frutas = ["manga", "banana", "jaca", "melancia"]
for fru in frutas:
  print(f"Eu gosto de {fru}.")
  if fru == "banana":
    break"""

# exemplo usando continue (pula pro proximo item)

"""veiculos = ["carro", "moto", "barco", "avião"]
for item in veiculos:
  if item == "barco":
    continue
  print(item)"""

"""#exibir apenas os numeros positivos de uma lista de valores

lista = [1, 7 , -3, 9, -1, -4, -7, 5, -10]
for num in lista:
  if num < 0:
    continue
   else:
    print("Repetição concluida")
else:
  """

"""# repetir uma frase 20 vezes
cont = 1
while cont <= 10 :
  print("Meu texto...")
  cont = cont + 1"""

"""# repetir 10 vezes usando for/range
for numero in range(5, 11):
  print(numero)"""

#repetir 10 vezes usando for/range

"""for numero in range(10):
  print("Minha frase legal...")"""

"""for x in range(1, 11):
  print(x)"""

"""for num in range(0,50+1,5):
  print(num)"""


# for dentro de outro for (encadeado/aninhado)
# imprimir as tabuadas de 1 até 10

"""for tab in range(1,11):
  for num in range (1,11):
    print(f"{tab} x {num} = {tab*num}")"""

# A escola irá ensaiar uma quadrilha junina.
# A professora quer saber todas as possibilidades de pares que podem ser formados entre os meninos e as meninas
# Faça um programa usando for encadeado para criar todas as combinações entre uma lista com os meninos e uma lista com as meninas

meninos = ["Alan", "Bruno", "Cláudio"]
meninas = ["Alice", "Bianca", "Celina", "Dotory"]

for boy in meninos:
  for girl in meninas:
    print(f"{boy} pode dançar com {girl}")
