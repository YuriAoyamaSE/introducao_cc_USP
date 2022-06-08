lista = []

while True:
    entrada = int(input("Digite um número: "))
    if entrada == 0:
        break
    lista.append(entrada)

for numero in lista[::-1]:
    print(numero)
