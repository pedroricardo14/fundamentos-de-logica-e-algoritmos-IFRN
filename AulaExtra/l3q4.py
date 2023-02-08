"""4) Digite as notas de uma prova para uma turma de 10 alunos e calcule a média da turma. Dica: use uma variável para acumular a soma de todas as notas, por último, já fora do laço, faça a divisão para calcular a média."""
soma = 0
cont = 1
while cont <= 10:
  nota = float(input(f"Digite a nota {cont}: "))
  soma += nota   #soma = soma + nota
  cont +=1          # cont = cont+1

media = soma/10
print("Média da turma = ", media)
