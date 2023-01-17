# Crie um jogo que sorteia um número entre 1 e 100 e permite ao usuário digitar diversos valores até acertar. Se o número for maior ou menor que o número sorteado, exibir uma mensagem com esta informação. Ao final, diga quantas tentativas o usuário fez para acertar.

import random 
sorteado = random.randint(1,100)
digitado = 0
tentativas = 0
while digitado != sorteado:
  digitado = int(input("Digite: "))
  tentativas = tentativas + 1

  if digitado == sorteado :
    print(f"Parabéns! Acertou em {tentativas} tentativa(s).")

  if digitado > sorteado :
    print("O número digitado é maior que o número sorteado.")
  if digitado < sorteado :
    print("O número digitado é MENOR  que o número sorteado.")
