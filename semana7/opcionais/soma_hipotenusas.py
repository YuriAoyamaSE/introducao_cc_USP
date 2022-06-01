def possui_catetos_int(h: int) -> bool:
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

def listar_hipotenusas(h: int) -> list[int]:
    list_h = []
    for i in range(1,h+1):
        if possui_catetos_int(i):
            list_h.append(i)
    return list_h
        
def soma_hipotenusas(n: int) -> int:
    soma = sum(listar_hipotenusas(n))
    return soma
