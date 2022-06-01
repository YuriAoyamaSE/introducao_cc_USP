linha = 1

while linha <= 10:
    coluna = 1
    while coluna <= 10:
        produto = linha * coluna
        print(produto, end = "\t")
        coluna += 1
    print()
    linha += 1