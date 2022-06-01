largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for a in range(altura):
    for l in range(largura):
        inner_l = l > 0 and l < largura - 1
        inner_a = a > 0 and a < altura - 1
        char = ' ' if (inner_l and inner_a) else "#"
        print(char, end='')
    print()
