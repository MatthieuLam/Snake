import sys
import pygame
import random

#Constant

x0 = 0
y0 = 0
width = 30
height = 30
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

# Helper Functions

def setup():
    #Setup
    width_height = [width*cell_size, height*cell_size]
    pygame.init()
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return screen, clock

def exit():
    pygame.quit()
    sys.exit()

def handle_events():
    # Event Management
    global direction
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

def move_snake():
    #Game Logic (move snake)
    global fruit, score, snake
    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    if (new_head in snake or new_head[0] < 0 or new_head[0] >= 30 or new_head[1] < 0 or new_head[1] >= 30):
        exit()
    elif new_head == fruit :
        score += 1
        snake = snake + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake = snake[1:] + [new_head]

def draw_frame(screen):
    #Frame Update
    screen.fill(colors["background"])
    for k in range(len(snake)) :
        rect = [snake[k][0]*cell_size, snake[k][1]*cell_size, cell_size, cell_size]
        pygame.draw.rect(screen, colors["snake"], rect)
    pygame.draw.rect(screen, colors["fruit"], [fruit[0]*cell_size, fruit[1]*cell_size, cell_size, cell_size])
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")
    
def wait_for_next_frame(clock):
    #Wait for next frame
    clock.tick(FPS)

#Setup & Main Loop

screen, clock = setup()
while True :
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)
