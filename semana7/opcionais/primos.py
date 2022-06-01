def verificar_primo(n):
    i = 2
    comum = False
    while i < n and not comum:
        if n % i == 0:
            comum = True
        i +=1
    return n > 0 and (not comum or n == 2)

def n_primos(n: int) -> int:
    primos = 0
    while n >= 2:
        primos +=1 if verificar_primo(n) else 0
        n -= 1
    return primos
