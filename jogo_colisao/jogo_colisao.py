 
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

#x = largura/2
#y = 0

pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load("BoxCat.mp3")
pygame.mixer.music.play(-1)

Som_colisao = pygame.mixer.Sound("coin.wav")
Som_colisao.set_volume(0.5)

x = int(largura/2)
y = int(altura/2)

x_azul = randint(40, 600)
y_azul = randint(50,430)

pontos = 0
font = pygame.font.SysFont('gabriola', 40, True, True) # fonte, negrito italico
# para procurar por fonts pygame.font.get_fonts()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))    # preenche a tela com o preto
    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (255,255,255)) # variavel, cerrilhado, cor
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #if event.type == KEYDOWN:
        #    if event.key == K_a:
        #        x = x - 20
        #    if event.key == K_d:
        #        x = x + 20
        #    if event.key == K_w:
        #        y = y - 20
        #    if event.key == K_s:
        #        y = y + 20  
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
        if(x <= 0):
            x = largura
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
        if(x >= 640):
            x = 0
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
        if(y <= 0):
            y = altura
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
        if(y >= 480):
            y = 0
        
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))   # cores rgb, posicao, tamanho
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))   # cores rgb, posicao, tamanho
    #pygame.draw.aaline(tela, (0,255,0),(100,200),(200,200))
    #pygame.draw.line(tela, (100,240,0),(550, 400),(600,450))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        Som_colisao.play()

    #if y >= altura:    movimenta o retangulo
    #    y = 0
    #
    #y = y + 5  

    #pygame.draw.circle(tela, (0,0,120), (300, 260), (40)) # cores rgb, posicao, diametro
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5) # cores rgb, posicao ponto,posicao do ponto, espessura
    tela.blit(texto_formatado, (450,40))
    pygame.display.update()