from math import sqrt


a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

d = b**2 - 4*a*c

if d == 0:
    print("a raiz desta equação é", -b/2*a)
elif d > 0:
    x = (-b + sqrt(d))/2*a
    y = (-b - sqrt(d))/2*a
    print(f"as raízes da equação são {min(x,y)} e {max(x,y)}")
else:
    print("esta equação não possui raízes reais")