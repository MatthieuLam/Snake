import sys
import pygame
import random

#Setup
pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

#Constant
x0 = 0
y0 = 0
width = 20
height = 20
cell_size = 20
Blanc = [255,255,255]
Noir = [0,0,0]
Rouge = [255, 0, 0]
FPS = 3
colors = {"background": Blanc, "snake": Noir, "fruit": Rouge}
UP = [0.0, -1.0]
LEFT = [-1.0, 0.0]
DOWN = [0.0, 1.0]
RIGHT = [1.0, 0.0]

# Game State
snake = [[10, 15],[11, 15],[12, 15],]
direction = [1,0]
fruit = [10,10]
score = 0

def exit():
    pygame.quit()
    sys.exit()




#Main Loop
while True :

    # Event Management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q :
                exit()
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    #Game Logic (move snake)
    head = snake[-1]
    tail = snake[0]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    if (new_head in snake or new_head[0] < 0 or new_head[0] >= 30 or new_head[1] < 0 or new_head[1] >= 30):
        exit()
    elif new_head == fruit :
        score += 1
        snake = snake + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake = snake[1:] + [new_head]

    #Frame Update
    screen.fill(colors["background"])
    for k in range(len(snake)) :
        rect = [snake[k][0]*cell_size, snake[k][1]*cell_size, width, height]
        pygame.draw.rect(screen, colors["snake"], rect)
    pygame.draw.rect(screen, colors["fruit"], [fruit[0]*cell_size, fruit[1]*cell_size, width, height])
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

    #Wait for next frame
    clock.tick(FPS)

    
