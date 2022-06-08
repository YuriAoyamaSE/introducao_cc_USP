def e_hipotenusa(h: int) -> bool:
    i = 1
    j = 1
    while i < h:
        j = 1
        i += 1
        while j < h:
            j +=1
            if (i**2 + j**2) == (h**2):
                return True
    return False
        
def soma_hipotenusas(n: int) -> int:
    soma = 0
    for i in range(1,n+1):
        if e_hipotenusa(i):
            soma += i
    return soma

for n in [6,15,20,25,27]:
    print(soma_hipotenusas(n))