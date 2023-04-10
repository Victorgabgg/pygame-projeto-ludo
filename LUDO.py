
import pygame
from pygame.locals import *
import random

black = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
blue = (0, 0, 255)

ts = 30


mapalist =[ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,0,6,6,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,6,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,0,6,0,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,6,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,6,0,0,0,0,0,0],
            [0,0,5,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,5,5,5,5,5,0,0,0,8,8,8,8,8],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
            [0,0,0,0,0,0,0,0,7,0,0,0,0,0,0],
            [0,0,4,0,4,0,0,0,7,0,0,3,0,3,0],
            [0,0,0,0,0,0,0,0,7,0,0,0,0,0,0],
            [0,0,4,0,4,0,0,0,7,0,0,3,0,3,0],
            [0,0,0,0,0,0,0,7,7,0,0,0,0,0,0] ] 
            

pygame.init()
tela = pygame.display.set_mode((500,500),0,32) 
pygame.display.set_caption('LUDO')
fim = False

while not fim:
    tela.fill((10, 150, 150))

    c = 25
    pygame.draw.rect(tela, (255, 255, 255), (10, 10, 480, 480), 0)

    j = 0
    while j < 15:
        i = 0
        while i < 15:
            pygame.draw.rect(tela, (0, 0, 0), (25+i*30, 25+j*30, 30, 30), 1)
            i += 1
        j += 1

    d = c + 30
    e = d + 10
    def desenha_tela():
        #Quadrados principais
        pygame.draw.rect(tela, r, [c, c, ts * 6, ts * 6])
        pygame.draw.rect(tela, g, [c + (ts * 9), c, ts * 6, ts * 6])
        pygame.draw.rect(tela, y, [c, c + (ts * 9),  (ts * 6), ts * 6])
        pygame.draw.rect(tela, blue, [c + (ts * 9), c + (ts * 9), ts * 6, ts * 6])
        pygame.draw.rect(tela, black, [c+ (ts * 6), c + (ts * 6), ts * 3, ts * 3])

        #Brancos no meio
        pygame.draw.rect(tela, w, [d, d, ts * 4, ts * 4])
        pygame.draw.rect(tela, w, [d + (ts * 9), d, ts * 4, ts * 4])
        pygame.draw.rect(tela, w, [d, d + (ts * 9),  (ts * 4), ts * 4])
        pygame.draw.rect(tela, w, [d + (ts * 9), d + (ts * 9), ts * 4, ts * 4])
        

        #Cores de dentro desenhando de maneira simplificada
        for i in range(0, len(mapalist)):
            for j in range(0, len(mapalist[i])):

                if mapalist[i][j] == 1:
                    pygame.draw.rect(tela, r, [30*j, 30*i, 50, 50])
                    pygame.draw.ellipse(tela, g, [33*j, 33*i, 30, 30])
                elif mapalist[i][j] == 2:
                    pygame.draw.rect(tela, g, [30*j, 30*i, 50, 50])
                    pygame.draw.ellipse(tela, r, [31*j, 33*i, 30, 30])
                elif mapalist[i][j] == 3:
                    pygame.draw.rect(tela, blue, [30*j, 30*i, 50, 50])
                    pygame.draw.ellipse(tela, y, [31*j, 31*i, 30, 30])
                elif mapalist[i][j] == 4:
                    pygame.draw.rect(tela, y, [30*j, 30*i, 50, 50])
                    pygame.draw.ellipse(tela, blue, [33*j, 31*i, 30, 30])        
                    #A partir daqui colorindo os espaços
                elif mapalist[i][j] == 5:
                    pygame.draw.rect(tela, r, [(30*j) - 4,(30*i) -4, 29, 29])
                elif mapalist[i][j] == 6:
                    pygame.draw.rect(tela, g, [(30*j) - 4,(30*i) -4, 29, 29])
                elif mapalist[i][j] == 7:
                    pygame.draw.rect(tela, y, [(30*j) - 4,(30*i) -4, 29, 29])
                elif mapalist[i][j] == 8:
                    pygame.draw.rect(tela, blue, [(30*j) - 4,(30*i) -4, 29, 29])


    desenha_tela()

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            fim = True

pygame.display.quit()

print("Fim do programa")
