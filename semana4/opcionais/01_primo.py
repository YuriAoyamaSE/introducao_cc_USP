n = int(input("Digite o valor de n: "))
i = 2
comum = False
while i < n and not comum:
    if n % i == 0:
        comum = True
    i +=1

if comum and n != 2:
    print("não primo")
else:
    print("primo")
