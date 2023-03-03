import pygame
import os
import random

pygame.init()

HEIGHT_TELA = 600
WIDTH_TELA = 1100
TELA = pygame.display.set_mode((WIDTH_TELA, HEIGHT_TELA))

dog_size = (180, 100)
szd_dog_1 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '1.png')), dog_size)
szd_dog_2 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '2.png')), dog_size)
szd_dog_3 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '3.png')), dog_size)
szd_dog_4 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '4.png')), dog_size)
szd_dog_5 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '5.png')), dog_size)
szd_dog_6 = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '6.png')), dog_size)

CASINHA = [pygame.transform.scale(pygame.image.load(os.path.join('Imagens', 'casinha.png')), (150, 100))]

PATINHO = [pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '1_-_pato.png')), (60, 60)),
           pygame.transform.scale(pygame.image.load(os.path.join('Imagens', '2_-_pato.png')), (60, 60))]

CORRENDO = [szd_dog_1, szd_dog_2, szd_dog_3, szd_dog_4, szd_dog_5, szd_dog_6]

PULANDO = [szd_dog_3]

ARVORE = [pygame.image.load(os.path.join('Imagens', '1_-_tree.png')),
          pygame.image.load(os.path.join('Imagens', '2_-_tree.png'))]

ARBUSTINHO = [pygame.transform.scale(pygame.image.load(os.path.join('Imagens', 'bush.png')), (110, 55))]

MOEDA = pygame.image.load(os.path.join('Imagens', 'coin.png'))

DIAMANTE = pygame.image.load(os.path.join('Imagens', 'diamante.png'))

NUVEM = pygame.transform.scale(pygame.image.load(os.path.join('Imagens', 'nuvem.png')), (200, 200))

FUNDO = pygame.image.load(os.path.join('Imagens', 'floor3.png'))

class Doguinho:

    X_POS = 80
    Y_POS = 451
    PULO_VEL = 10
    
    def __init__(self):
        #CHAMAR OS FRAMES DO CACHORRO CORRENDO E PULANDO
        self.correr_img = CORRENDO
        self.pular_img = PULANDO
        
        #DEFINIR A CORRIDA PARA TRUE E O PULO PARA FALSO, JÁ QUE O CACHORRO POR PADRÃO VAI ESTAR CORRENDO
        self.dog_correr = True
        self.dog_pular = False
        
        #DEFINIR A HITBOX DO CACHORRO
        self.step_index = 0
        self.pulo_vel = self.PULO_VEL
        self.image = self.correr_img[0]
        self.dog_rect = (self.image.get_rect())
        self.dog_rect.x = self.X_POS
        self.dog_rect.y = self.Y_POS
    
    def update(self, userInput):
        
        #FUNCAO PARA ATUALIZAR O CACHORRO A CADA LOOP
        
        if self.dog_correr:
            self.correr()
            
        if self.dog_pular:
            self.pular()
    
        if self.step_index >= 12:
            self.step_index = 0
        
        #FAZER O CACHORRO PULAR MUDANDO DE ANIMACAO QUANDO APERTAR K_UP ou SPACE
        
        if userInput[pygame.K_UP] and not self.dog_pular:
            self.dog_correr = False
            self.dog_pular = True

        elif userInput[pygame.K_SPACE] and not self.dog_pular:
            self.dog_correr = False
            self.dog_pular = True

        elif not (self.dog_pular or userInput[pygame.K_DOWN]):
            self.dog_pular = False
            self.dog_correr = True

    def correr(self):
        self.image = self.correr_img[self.step_index // 2]
        self.dog_rect = self.image.get_rect()
        self.dog_rect.x = self.X_POS
        self.dog_rect.y = self.Y_POS
        self.step_index += 1

    def pular(self):
        self.image = self.pular_img[0]
        if self.dog_pular:
            self.dog_rect.y-= self.pulo_vel * 4
            self.pulo_vel -= 0.8
        if self.pulo_vel < - self.PULO_VEL:
            self.dog_pular = False
            self.pulo_vel = self.PULO_VEL
            
        
    def tela(self, TELA):
        TELA.blit(self.image, (self.dog_rect.x, self.dog_rect.y))
            
class Nuvem:
    def __init__(self):
        self.x = WIDTH_TELA + random.randint(800, 1000)
        self.y = random.randint(30, 200)
        self.image = NUVEM
        self.width = self.image.get_width()
        
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = WIDTH_TELA + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
        
    def tela(self, TELA):
        TELA.blit(self.image, (self.x, self.y))

class Obstaculo:
    def __init__(self, IMAGE, TIPO):
        self.image = IMAGE
        self.tipo = TIPO
        self.rect = self.image[self.tipo].get_rect()
        self.rect.x = WIDTH_TELA

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obs.pop()

    def tela(self, TELA):
        TELA.blit(self.image[self.tipo], self.rect)

class Casinha(Obstaculo):
    def __init__(self, IMAGE):
        self.TIPO = 0 #random.randint(0, 2) acredito q é pra escolher entre os cactus
        super().__init__(IMAGE, self.TIPO)
        self.rect.y = 450

class Arbustinho(Obstaculo):
    def __init__(self, IMAGE):
        self.TIPO = 0 #random.randint(0, 2) acredito q é pra escolher entre os cactus
        super().__init__(IMAGE, self.TIPO)
        self.rect.y = 500
        #A COORDENADA DE Y PRO OBJETO TEM Q SER A ALTURA DELE PRA FUNCIONAR A HITBOX

class Patinho(Obstaculo):
    def __init__(self, IMAGE):
        self.TIPO = 0
        super().__init__(IMAGE, self.TIPO)
        self.rect.y = 490 #onde o pato aparece em y
        self.index = 0

    def tela(self, TELA):
        #alterna a imagem do patinho entre levantado e agachado
        if self.index >= 9:
            self.index = 0
        TELA.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_fundo, y_pos_fundo, points, obs
    run = True
    clock = pygame.time.Clock()
    player = Doguinho()
    nuvem = Nuvem()
    game_speed = 30
    obs = []
    x_pos_fundo = 0
    y_pos_fundo = 550
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    contador_morte = 0


    def score():
        #pontuacao do jogador
        global points, game_speed, x_pos_fundo, y_pos_fundo
        #aumentar um ponto
        points+=1
        #aumentar a velocidade do jogo a cada 100 pontos
        if points % 100 == 0:
            game_speed +=1

        text = font.render('Pontos: ' + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        #posicionando o placar de pontos
        textRect.center = (1000, 40)
        TELA.blit(text, textRect)

    def background():
        global x_pos_fundo, y_pos_fundo
        image_width = FUNDO.get_width()
        TELA.blit(FUNDO, (x_pos_fundo, y_pos_fundo))
        TELA.blit(FUNDO, (image_width + x_pos_fundo, y_pos_fundo))
        if x_pos_fundo <= -image_width:
            TELA.blit(FUNDO, (image_width + x_pos_fundo, y_pos_fundo))
            x_pos_fundo = 0
        x_pos_fundo -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        TELA.fill((153, 217, 234))       
        userInput = pygame.key.get_pressed()
        
        player.tela(TELA)
        player.update(userInput)   

        if len(obs) == 0:
            if random.randint(0, 2) == 0:
                obs.append(Arbustinho(ARBUSTINHO))
            elif random.randint(0, 2) == 1:
                obs.append(Casinha(CASINHA))
            elif random.randint(0, 2) == 2:
                obs.append(Patinho(PATINHO))

        for o in obs:
            o.tela(TELA)
            o.update()
            if player.dog_rect.colliderect(o.rect):
                pygame.time.delay(700) #em milisegundos
                contador_morte +=1
                menu(contador_morte)

        background()
        
        nuvem.tela(TELA)
        nuvem.update()

        score()

        clock.tick(30)
        pygame.display.update()
    pygame.quit()

def menu(contador_morte):

    global points
    run = True
    while run:
        TELA.fill((153, 217, 234))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if contador_morte == 0:
            text = font.render("Pressione qualquer botao para iniciar", True, (0, 0, 0,))

        elif contador_morte >= 1:
            text = font.render("Pressione qualquer botao para reiniciar", True, (0, 0, 0,))
            score = font.render(f"Sua pontuacao: {points}", points, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (WIDTH_TELA // 2, HEIGHT_TELA // 2 + 50)
            TELA.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (WIDTH_TELA // 2, HEIGHT_TELA // 2)
        TELA.blit(text, textRect)
        TELA.blit(CORRENDO[2], (WIDTH_TELA // 2 - 20, HEIGHT_TELA // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(contador_morte = 0)


