x = int(input("Digite um númerointeiro: "))
anterior = '' 
numeros_iguais = False
while x > 0 and not numeros_iguais:
    anterior = x % 10
    x //= 10
    if anterior == x % 10:
        numeros_iguais = True
if numeros_iguais:
    print("sim")
else:
    print('não')