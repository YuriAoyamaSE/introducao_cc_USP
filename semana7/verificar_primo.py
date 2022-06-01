def verificar_primo(n):
    i = 2
    comum = False
    while i < n and not comum:
        if n % i == 0:
            comum = True
        i +=1
    return n > 0 and (not comum or n == 2)

n = 1

while n > 0:
    n = int(input("Digite um número inteiro: "))
    resultado = " é " if verificar_primo(n) else " não é "
    print(f'{n} {resultado} primo')


"""
def verificar_primo(n):
    fator = 2
    while n % fator != 0 and fator <= n/2:
        fator += 1
    return n % fator != 0
    
"""