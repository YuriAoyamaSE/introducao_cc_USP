n = int(input('Digite um número inteiro: '))

fator = 2
resultado = []
print(f"Decomposição do número {n}:")

while n > 1:
    multiplicidade = 0
    while n % fator == 0:
        multiplicidade += 1
        n /= fator
    if multiplicidade > 0:
        #print(f"fator {fator} multiplicidade = {multiplicidade}")
        resultado.append([fator,multiplicidade])
    fator +=1

for i,j in resultado:
    separador = "" if [i,j] == resultado[-1] else " + "
    print(f"{i}^{j}", end = separador)
    