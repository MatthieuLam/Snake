import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
#clock = pygame.time.Clock()

x0 = 0
y0 = 0
width = 20
height = 20
B = [255,255,255]
N = [0,0,0]

while True :
    snake = [[10, 15],[11, 15],[12, 15],]
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
            rect = [x, y, width, height]
            pygame.draw.rect(screen, B , rect)
    for k in range(len(snake)) :
        rect = [snake[k][0]*20, snake[k][1]*20, width, height]
        pygame.draw.rect(screen, N , rect)
    pygame.display.update()
    

    
