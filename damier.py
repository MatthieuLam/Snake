import pygame
import sys

x0 = 0
y0 = 0
width = 20
height = 20
N = [0,0,0]
B = [255,255,255]
pygame.init()
screen = pygame.display.set_mode([600, 600])
#clock = pygame.time.Clock()


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q :
                pygame.quit()
                sys.exit()
    for i in range(30):
        x = x0 + i*20
        for j in range (30):
            y = y0 + j*20
            if (i+j)%2 == 0 :
                rect = [x, y, width, height]
                pygame.draw.rect(screen, B , rect)
                pygame.display.update()
    #clock.tick()


