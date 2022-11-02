import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

x0 = 0
y0 = 0
width = 20
height = 20
B = [255,255,255]
N = [0,0,0]
snake = [[10, 15],[11, 15],[12, 15],]
direction = [1,0]


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q :
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                direction = [0.0, -1.0]
            elif event.key == pygame.K_LEFT:
                direction = [-1.0, 0.0]
            elif event.key == pygame.K_DOWN:
                direction = [0.0, 1.0]
            elif event.key == pygame.K_RIGHT:
                direction = [1.0, 0.0]
    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    snake = snake[1:] + [new_head]
    screen.fill(B)
    for k in range(len(snake)) :
        rect = [snake[k][0]*20, snake[k][1]*20, width, height]
        pygame.draw.rect(screen, N , rect)
    pygame.display.update()
    clock.tick(1)

    
