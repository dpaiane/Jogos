import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura/2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')
relogio = pygame.time.Clock()

while True:
     relogio.tick(30)
     tela.fill((0,0,0))
     for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

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

     pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
     pygame.draw.circle(tela, (0,255,0), [60, 250], 40)


     pygame.display.update()