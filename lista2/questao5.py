"""5) Escreva um programa que informa sobre a aprovação de um empréstimo habitacional. O usuário informa o
valor da casa, o salário e a quantidade de anos a pagar. O valor da prestação não pode ser superior a 30% do
salário. Informe o valor da prestação e se o empréstimo será aprovado ou não. Não são considerados juros
neste exemplo."""

imovel = float(input("Valor do imóvel: "))
salario = float(input("Salario: "))
tempo = float(input("Tempo(anos): "))

prestacao = imovel / (tempo*12)

salario30 = salario * 30/100

if prestacao <= salario30: 
  print("Emprestimo aprovado.")
  print(f"Parcela = R$ {prestacao}")
else :
  print("Emprestimo negado.")
  print(f"Parcela = R$ {prestacao}")
  print(f"Limite R$ {salario30}") 
