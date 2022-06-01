from math import sqrt

def calcula_delta(a,b,c):
    return b**2 - 4*a*c

def imprime_raizes(a,b,c):
    delta = calcula_delta(a,b,c)
    if delta == 0:
        raiz1 = (-b + sqrt(delta)) / (2*a)
        print("A única raíz é: ", raiz1)
    elif delta < 0:
        print("Essa equação não possui raízes reais.")
    else:
        raiz1 = (-b + sqrt(delta)) / (2*a)
        raiz2 = (-b - sqrt(delta)) / (2*a)
        print(f"As raízes são {raiz1} e {raiz2}")
    
def main():
    a = float(input("Informe o valor de a: "))
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))
    imprime_raizes(a,b,c)


main()
