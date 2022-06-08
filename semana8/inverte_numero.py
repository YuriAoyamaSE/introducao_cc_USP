lista = []

while True:
    entrada = int(input("Digite um número inteiro: "))
    if entrada == 0:
        break
    lista.append(entrada)

print(lista[::-1])
