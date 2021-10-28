def computador_escolhe_jogada(n, m):
    jogada = m
    if m > n:
        jogada = n
    else:
        x = n % (m+1)
        if x > 0:
            jogada = x
    
        else:
            jogada = m
    
    return jogada


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar?"))
    while jogada > m or jogada > n or 0 == jogada or 1 > jogada:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada = int(input("Quantas peças você vai tirar?"))
    if jogada > 1:
        print('Você tirou ',jogada,' peças')
    elif jogada == 1:
        print('Você tirou uma peça.')
    
    return jogada

#


def partida():
        
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))
        while m>n:
            print('numero de peca invalido')
            m = int(input('Limite de peças por jogada?'))
        
            # ###### QUANDO O Player COMECA##########
        if n % (m + 1) == 0:
           print('Voce começa!') 
           while n > 0:
                
                jogada = usuario_escolhe_jogada(n, m)
                n= n - jogada 
                if n > 1: 
                    print('Agora restam',n, 'peças no tabuleiro')
                if n == 1: 
                    print('Agora resta apenas uma peça no tabuleiro.')
                if n == 0:
                    print('Você ganhou!')
                  
                    break
                jogada = computador_escolhe_jogada(n, m)
                n= n - jogada 
                print('PC tira',jogada)
                print('Agora restam',n, 'peças no tabuleiro')
                if n == 0:
                    print('Fim do jogo! O computador ganhou!')
                    
                    break
                         
           
        else:
            print('Computador começa!')
            while n > 0:
                jogada = computador_escolhe_jogada(n, m)
                n= n - jogada 
                print('PC tira',jogada)
                print('Agora restam',n, 'peças no tabuleiro')
                if n == 0:
                    print('Fim do jogo! O computador ganhou!')
                    
                    break 
                jogada = usuario_escolhe_jogada(n, m)
                n= n - jogada 
                if n > 1: 
                    print('Agora restam',n, 'peças no tabuleiro')
                if n == 1: 
                    print('Agora resta apenas uma peça no tabuleiro.')
                if n == 0:
                    print('Você ganhou!')
                    break
                   
              
           
def campeonato():
    
    camp = 1
    while camp <= 3:
        print('**** Rodada',camp, '****')
        partida()
        camp = camp + 1

    
    print('**** Final do campeonato! ****')
    print('Placar: Você','0 X 3',' Computador')
    
print('Bem-vindo ao jogo do NIM! Escolha')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato 2')
x = int(input("Digite a opcao desejada "))
while x != 1 and x != 2:
    print('Opcao invalida')
    x = int(input("Digite a opcao desejada "))
if x == 1:
    print('Voce escolheu uma partida isolada!')
    partida()
    
    print('funcionando apos partida')
elif x == 2:
    print('Voce escolheu um campeonato!')
    campeonato()
    
print('FIM')