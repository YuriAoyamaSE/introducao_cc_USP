def validar_primo(n):
    i = 2
    comum = False
    while i < n and not comum:
        if n % i == 0:
            comum = True
        i +=1
    return not comum   

def maior_primo(n):
    while not validar_primo(n):
        n -= 1
    return n