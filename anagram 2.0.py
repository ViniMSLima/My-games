'''JOGO DO ANAGRAMA'''
'''começa com 100 pontos e desconta 10 a cada tentativa'''
'''3 dificuldades com quantidade de letras'''
import random as rd

print('ANAGRAMA')
points = 100
recorde = 0
contador = 0
while True:
    try:
        dif = int(input('1 - facil\n2 - medio\n3 - dificil\n\nSelecione uma dificuldade\n>'))
        
        while dif < 1 or dif > 3:
            print('Valor incorreto, selecione entre < 1 >, < 2 > e < 3 >')
            dif = int(input('Selecione uma dificuldade\n1 - facil\n2 - medio\n3 - dificil\n>'))  
        if dif == 1:
            linha = rd.randint(1,200)
            deducao = 10
            tentativas = 10
        if dif == 2:
            linha = rd.randint(201,400)
            deducao = 20
            tentativas = 5
        if dif == 3:
            linha = rd.randint(401,600)
            deducao = 25
            tentativas = 4
        with open('palavras.txt','r') as txt:
            texto = txt.read()
            palavras = texto.split()
            word = palavras[linha]
            embaralhas=rd.sample(word, len(word))
            juntar_embaralhas = ''.join(embaralhas)
            print(juntar_embaralhas)
        for i in range(tentativas):
            print(f'Pontos> {points}')
            palpite = input('Palpite\n> ')
            if palpite == 'amogus':
                print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁''''')    
            if palpite != word:
                points-=deducao
            else:
                print('Você acertou!')
                print(f'A palavra era: {word}')
                points = 100
                contador+=1
                break
        if points == 0:
            print(f'Você perdeu!\nA palavra era: {word}')
            contador = 0
            points = 100
        if contador > recorde:
            print(f'Seu recorde foi: {contador}')
            recorde = contador
        else:
            print(f'Recorde atual: {recorde}')
        print('\nDeseja jogar novamente?')
        again = input('Para fechar o jogo digite < 0 >\nPara continuar jogando aperte <ENTER>\n> ')
        if again == '0':
            print('\nJogo fechando...\nAté mais!')
            break
                
    except ValueError:
        print('Valor incorreto, favor digitar um número!')
    except:
        print('\nErro, reiniciando sistema...')
        break