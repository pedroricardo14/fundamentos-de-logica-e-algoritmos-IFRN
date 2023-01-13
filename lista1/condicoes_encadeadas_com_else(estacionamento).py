tempo = int(input("Tempo de permanência? "))
veiculo = input("Qual o veículo? ")

if tempo <= 10 : 
  print("GRATIS! :)")
else : 
  if veiculo == "moto" : 
    print("Tarifa R$ 1,50")
  else :
    print("Tarifa R$ 3,00")
    
