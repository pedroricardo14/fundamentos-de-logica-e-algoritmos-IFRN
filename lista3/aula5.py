# um sensor alerta se a tenmperatura estiver incorreta se for abaixo de 5 graus ou acima de 15 graus

temp = float(input("Temperatura? "))

if temp < 5 or temp > 15 : 
  print("Temperatura inadequada.")
else:
  print("Temperatura correta.")

#O "or" é parecido com o and. A diferença é que ele funciona mesmo quando a resposta de um é não e a do outro é sim.
  
