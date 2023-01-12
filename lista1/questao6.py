"""6) Em uma eleição sindical concorreram ao cargo de presidente três candidatos (A, B e C). Durante a apuração
dos votos foram computados votos nulos e votos em branco, além dos votos válidos para cada candidato. Deve
ser criado um programa de computador que efetue a leitura da quantidade de votos válidos para cada
candidato, além de efetuar também a leitura da quantidade de votos nulos e votos em branco. Ao final o
programa deve apresentar o número total de eleitores, considerando votos válidos, nulos e em branco; o
percentual correspondente de votos válidos em relação à quantidade de eleitores; o percentual correspondente
de votos válidos de cada candidato em relação à quantidade de eleitores, além do percentual de votos brancos
e votos nulos; """

cand_a = int(input("Cand. A: "))
cand_b = int(input("Cand. B: "))
cand_c = int(input("Cand. C: "))
branco = int(input("Brancos: "))
nulos = int(input("Nulos: "))

total = cand_a + cand_b + cand_c + branco + nulos
print(f"Total de eleitores : {total}")

validos = ((cand_a + cand_b + cand_c)/total)*100
print(f"Votos válidos: {validos:.1f}%")

print(f"Cand. A: {cand_a/total*100:.1f}%")
print(f"Cand. B: {cand_b/total*100:.1f}%")
print(f"Cand. C: {cand_c/total*100:.1f}%")
print(f"Brancos: {branco/total*100:.1f}%")
print(f"Nulos: {nulos/total*100:.1f}%")
