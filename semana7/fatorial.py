def fatorial(n: int) -> int:
    fat = 1
    while n > 1:
        fat *= n
        n -=1
    return fat

n = 1
while n > 0:
    n = int(input("Digite 0 para sair ou um número para devolver seu fatorial: "))
    print(f"Fatorial de {n} = {fatorial(n)}")

print("FIM")
