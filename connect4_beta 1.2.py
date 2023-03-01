'''LIG-4'''
from colorama import Fore

Tabuleiro = [['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','',''],
             ['','','','','','','']]

linhas = 6
colunas = 7

def printTabuleiro():
    print('\n     1    2    3    4    5    6    7  ',end ='')
    for x in range(linhas):
        print("\n   ├────┼────┼────┼────┼────┼────┼────┤")
        print('   │', end ='')
        for y in range(colunas):
            if(Tabuleiro[x][y] =='O'):
                print(' ', Fore.MAGENTA + Tabuleiro[x][y] + Fore.RESET, end=' │')
            elif (Tabuleiro[x][y] =='0'):
                print(' ', Fore.CYAN + Tabuleiro[x][y] + Fore.RESET, end=' │')
            else:
                print(' ',  Fore.RESET + Tabuleiro[x][y], end='  │')
    print("\n   └────┴────┴────┴────┴────┴────┴────┘")

def verificarV(ficha):
    #verificar verticais
    for i in range(3):
        for j in range(4):
            if(Tabuleiro[i][j] == ficha and Tabuleiro[i+1][j] == ficha and Tabuleiro[i+2][j] == ficha and Tabuleiro[i+3][j] == ficha):
                
                return True
    #verificar horizontais
    for i in range(6):
        for j in range(4):
            if(Tabuleiro[i][j] == ficha and Tabuleiro[i][j+1] == ficha and Tabuleiro[i][j+2] == ficha and Tabuleiro[i][j+3] == ficha):
                return True
    
    #verificar diagonas baixo para cima
    for k in range(3):
        for i in range(3):
            for j in range(4):
                if(Tabuleiro[i][j] == ficha and Tabuleiro[i+1][j-1] == ficha and Tabuleiro[i+2][j-2] == ficha and Tabuleiro[i+3][j-3] == ficha):
                    return True
                     
    #verificar diagonais cima para baixo
    for k in range(3):
        for i in range(3):
            for j in range(4):
                if(Tabuleiro[i][j+k] == ficha and Tabuleiro[i+1][j+1+k] == ficha and Tabuleiro[i+2][j+2+k] == ficha and Tabuleiro[i+3][j+3+k] == ficha):
                                   
                    return True
def jogadorVez(jogador):
    #Verifica quam e o jogador da vez
    if jogador % 2 == 0:
        Ficha = 'O'
    else:
        Ficha = '0'
    return Ficha

def coordenadas(posicao_selecionada, jogador):
    #Coloca ficha no lugar selecionado
    Ficha = jogadorVez(jogador)
    linha = posicaoVazia(posicao_selecionada)
    if linha < 0:
        return False
    Tabuleiro[linha][posicao_selecionada] = Ficha

def posicaoVazia(coluna):
    #Verifica as posicoes da coluna pra empilhar as fichas
    linha=5
    while True:  
        if(Tabuleiro[linha][coluna] == '0') or (Tabuleiro[linha][coluna] == 'O'):  
            linha-=1
        else:
            return linha
#JOGO
jogador = 0
while True:
    if jogadorVez(jogador) == 'O':
        print(Fore.MAGENTA + '\n  --------------JOGADOR-1---------------', Fore.RESET)
    else:
        print(Fore.CYAN + '\n  --------------JOGADOR-2---------------'+ Fore.RESET)
    printTabuleiro()
    while True:
        try:
            selecao = int(input('Selecione uma coluna\n> '))
            while selecao < 1 or selecao > 7:
                print('Erro...\nColuna invalida')
                selecao = int(input('\nSelecione uma coluna\n> '))
            break
        except ValueError:
            print('Erro...\nDigite o valor de uma coluna valida')
    coordenadas(selecao - 1, jogador)
    
    verificarV('O')
    verificarV('0')
    
    if verificarV('O') or verificarV('0'):
        printTabuleiro()
        Ficha = jogadorVez(jogador)
        if Ficha == '0':
            print('Fim de jogo',Fore.CYAN + Ficha  + Fore.RESET, 'venceu!!!') 
        else:
            print('Fim de jogo',Fore.MAGENTA + Ficha + Fore.RESET, 'venceu!!!') 
        break
    jogador+=1