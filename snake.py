import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

x0 = 0
y0 = 0
width = 20
height = 20
B = [255,255,255]
N = [0,0,0]
R = [255, 0, 0]
snake = [[10, 15],[11, 15],[12, 15],]
direction = [1,0]
fruit = [10,10]
score = 0

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
    tail = snake[0]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    if (new_head in snake or new_head[0] < 0 or new_head[0] >= 30 or new_head[1] < 0 or new_head[1] >= 30):
        pygame.quit()
        sys.quit
    elif new_head == fruit :
        score += 1
        snake = snake + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake = snake[1:] + [new_head]
    screen.fill(B)
    for k in range(len(snake)) :
        rect = [snake[k][0]*20, snake[k][1]*20, width, height]
        pygame.draw.rect(screen, N , rect)
    pygame.draw.rect(screen, R, [fruit[0]*20, fruit[1]*20, width, height])
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")
    clock.tick(3)

    
