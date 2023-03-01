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
        print("\n   +----+----+----+----+----+----+----+")
        print('   |', end ='')
        for y in range(colunas):
            if(Tabuleiro[x][y] =='O' or Tabuleiro[x][y] =='X'):
                print(' ', Fore.RED + Tabuleiro[x][y], end=' |')
            else:
                print(' ', Fore.WHITE + Tabuleiro[x][y], end='  |')
    print("\n   +----+----+----+----+----+----+----+")

def verificarV(ficha):
    #verificar horizontais
    for y in range(linhas):
        for x in range(colunas - 3):
            if(Tabuleiro[x][y] == ficha and Tabuleiro[x+1][y] == ficha and Tabuleiro[x+2][y] == ficha and Tabuleiro[x+3][y] == ficha):
                print('Fim de jogo', ficha, 'venceu!!!')
                return True
    #verificar verticais
    for y in range(linhas):
        for x in range(colunas - 3):
            if(Tabuleiro[x][y] == ficha and Tabuleiro[x][y+1] == ficha and Tabuleiro[x][y+2] == ficha and Tabuleiro[x][y+3] == ficha):
                print('Fim de jogo', ficha, 'venceu!!!')
                return True
    #verificar diagonais
    for y in range(linhas - 3):
        for x in range(3, colunas):
            if(Tabuleiro[x][y] == ficha and Tabuleiro[x+1][y-1] == ficha and Tabuleiro[x+2][y-2] == ficha and Tabuleiro[x+3][y-3] == ficha):
                print('Fim de jogo', ficha, 'venceu!!!')
                return True
    for y in range(linhas - 3):
        for x in range(colunas - 3):
            if(Tabuleiro[x][y] == ficha and Tabuleiro[x+1][y+1] == ficha and Tabuleiro[x+2][y+2] == ficha and Tabuleiro[x+3][y+3] == ficha):
                print('Fim de jogo', ficha, 'venceu!!!')
                return True
    return False

def coordenadas(posicao_selecionada, jogador1):
    if jogador % 2 == 0:
        Ficha = 'O'
    else:
        Ficha = 'X'
    linha = posicaoVazia(posicao_selecionada)
    while linha == 'cheio':
        linha = posicaoVazia(int(input('\nSelecione a coluna\n> ')))
    Tabuleiro[linha][posicao_selecionada] = Ficha
    try:
        Tabuleiro[linha].remove(linha-1)
    except ValueError:
        return False

def posicaoVazia(coluna):
    linha=5
    while True:  
        if(Tabuleiro[linha][coluna] == 'X') or (Tabuleiro[linha][coluna] == 'O'):  
            linha-=1
        else:
            return linha
    print('Coluna cheia, selecione outra!')
    return 'cheio'

jogador = 0
while True:
    printTabuleiro()
    selecao = int(input('Selecione uma coluna\n> '))
    coordenadas(selecao, jogador)
    jogador+=1
    printTabuleiro()
    




















# Encerrar = False
# contadorvez = 0
# while(Encerrar == False):
#     if(contadorvez % 2 == 0):
#         printTabuleiro()
#         #JOGADOR 1
#         while True:
#             posicao_selecionada = input("\nChoose a space: ")
#             coordenada = coordenadas(posicao_selecionada)
#             try:
#         ### Verificar se está vazio
#                 if(posicaoVazia(coordenada) and gravidade(coordenada)):
#                     mudarVez(coordenada, '🔵')
#                     break
#                 else:
#                     print('Coordenada inválida')
#             except ValueError:
#                 print("Erro. Tente novamente.")
#         vencedor = verificarV('🔵')
#         contadorvez += 1
#     #JOGADOR 2 
#     else:
#        while True:
#            posicao_selecionada = input("\nChoose a space: ")
#            coordenada = coordenadas(posicao_selecionada)
#            try:
#        ### Verificar se está vazio
#                if(posicaoVazia(coordenada) and gravidade(coordenada)):
#                    mudarVez(coordenada, '🔴')
#                    break
#                else:
#                    print('Coordenada inválida')
#            except:
#                print("Erro. Tente novamente.")
#        vencedor = verificarV('🔴')
#        contadorvez += 1

#     if(vencedor):
#         printTabuleiro()
#         break
