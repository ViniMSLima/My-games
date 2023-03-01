'''LIG-4'''

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
        print('\n   |____|____|____|____|____|____|____|')
        print('   |', end ='')
        for y in range(colunas):
            if(Tabuleiro[x][y] =='🔵' or Tabuleiro[x][y] =='🔴'):
                print(x,'', Tabuleiro[x][y], end=' |')
            else:
                print(' ', Tabuleiro[x][y], end='  |')
    print('\n   |____|____|____|____|____|____|____|')
                
def mudarVez(posicao, vez):
    Tabuleiro[posicao[0]][posicao[1]] = vez
    
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

def coordenadas(inputInt):
    

def posicaoVazia(coordenada_desejada):
    if(Tabuleiro[coordenada_desejada[0]][coordenada_desejada[1]] == '🔴'):  
        return False
    if(Tabuleiro[coordenada_desejada[0]][coordenada_desejada[1]] == '🔵'):  
        return False
    else:
        return True

def gravidade(coordenada_desejada):
  ### Calcular espaço abaixo
  abaixo = [None] * 2
  abaixo[0] = coordenada_desejada[0] + 1
  abaixo[1] = coordenada_desejada[1]
  ### Coordenada tá no chão?
  if(abaixo[0] == 6):
    return True
  ### Verificar se tem uma ficha embaixo
  if(posicaoVazia(abaixo) == False):
    return True
  return False
            
Encerrar = False
contadorvez = 0
while(Encerrar == False):
    if(contadorvez % 2 == 0):
        printTabuleiro()
        #JOGADOR 1
        while True:
            posicao_selecionada = input("\nChoose a space: ")
            coordenada = coordenadas(posicao_selecionada)
            try:
        ### Verificar se está vazio
                if(posicaoVazia(coordenada) and gravidade(coordenada)):
                    mudarVez(coordenada, '🔵')
                    break
                else:
                    print('Coordenada inválida')
            except ValueError:
                print("Erro. Tente novamente.")
        vencedor = verificarV('🔵')
        contadorvez += 1
    #JOGADOR 2 
    else:
       while True:
           posicao_selecionada = input("\nChoose a space: ")
           coordenada = coordenadas(posicao_selecionada)
           try:
       ### Verificar se está vazio
               if(posicaoVazia(coordenada) and gravidade(coordenada)):
                   mudarVez(coordenada, '🔴')
                   break
               else:
                   print('Coordenada inválida')
           except:
               print("Erro. Tente novamente.")
       vencedor = verificarV('🔴')
       contadorvez += 1

    if(vencedor):
        printTabuleiro()
        break