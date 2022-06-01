x = int(input("Digite um número inteiro: "))
soma = 0 
while x > 0:
    soma += x % 10
    x //= 10
print(soma)