def computador_escolhe_jogada(n, m):
    jogada = n % (m+1)
    if jogada > m or jogada == 0:
        jogada = m
    return jogada

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("Você começa!")
        vez = 1
    else:
        print("Computador começa!")
        vez = -1
    while n > 0:
        if vez == 1:
            removidas = usuario_escolhe_jogada(n,m)
            quem = "Você"
        else:
            removidas = computador_escolhe_jogada(n,m)
            quem = "O computador"
        
        if removidas == 1:
            print(f"{quem} tirou uma peça.")
        else:
            print(f"{quem} tirou {removidas} peças.")
            
        vez *= -1
        n -= removidas
        
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n > 0:
            print(f"Agora restam apenas {n} peças no tabuleiro.")
        
    if vez == 1:
        print("Fim do jogo! O computador ganhou!")
        return "Computador"
    else:
        print("Fim do jogo! Você ganhou!")
        return "Você"

def campeonato():
    pt_usuario = 0
    pt_computador = 0
    for i in range(1,4):
        print(f"**** Rodada {i} ****")
        vitoria = partida()
        if vitoria == "Você":
            pt_usuario += 1
        else:
            pt_computador += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {pt_usuario} X {pt_computador} Computador")


if __name__ == '__main__':
    escolha = int(input(
        """Bem-vindo ao jogo do NIM! Escolha:
        
1 - para jogar uma partida isolada 
2 - para jogar um campeonato """))
    if escolha == 1:
        partida()
    elif escolha == 2:
        campeonato()