import pygame
import time
import random
YELLOW = (255, 228, 196)
BLUE = (30, 144, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 117.6
HEIGHT = 117.6
MARGIN = 3
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.init()
win = pygame.display.set_mode((900, 800))
win.fill(YELLOW)
move = [[WIDTH, 0], [-HEIGHT, 0], [0, -WIDTH], [0, HEIGHT]]
random_x = [368, 486, 590]
random_y = [200, 318, 436, 545]
cat_randomx = random.choice(random_x)
cat_randomy = random.choice(random_y)
cat_random = (cat_randomx, cat_randomy)
mouse_randomx = 486
mouse_randomy = 436
mouse_random = (mouse_randomx, mouse_randomy)
step = 0
grid = []
moves = 0
endMove = 20
for row in range(6):
    grid.append([])
    for column in range(6):
        grid[row].append(0)
grid[2][0] = 1
def checkmove():
    if moves == endMove:
        game_over()
        pygame.quit()
def movement():
    checkmove()
    i, j = random.choice(move)
    global mouse_random, mouse_randomy, mouse_randomx
    mouse_randomy += j
    mouse_randomx += i
    mouse_random = (mouse_randomx, mouse_randomy)
def background_blue():
    for row in range(6):
        for column in range(6):
            color = BLUE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * (column + 0.82) + MARGIN,
                              (MARGIN + HEIGHT) * (row + 0.4) + MARGIN,
                              WIDTH,
                              HEIGHT])
def background_green():
    for row in range(4):
        for column in range(4):
            color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * (column + 1.82) + MARGIN,
                              (MARGIN + HEIGHT) * (row + 1.4) + MARGIN,
                              WIDTH,
                              HEIGHT])
def game_over():
    time.sleep(0.2)
    win.fill(BLACK)
    Game_over = pygame.image.load('over.png')
    win.blit(Game_over, (50, 100))
    time.sleep(1)
    sound_obj = pygame.mixer.Sound('Game_over.mp3')
    sound_obj.play()
    time.sleep(4)
    sound_obj.stop()

pygame.display.update()
exit = False
while not exit:
    if step == 0:
        time.sleep(0.5)
        movement()
        checkmove()
        moves += 1
    pygame.draw.rect(win, BLACK, [102, 52, 718, 718])
    background_blue()
    background_green()
    image = pygame.image.load('cat2.png')
    win.blit(image, (cat_randomx, cat_randomy))
    image2 = pygame.image.load('mouse.png')
    win.blit(image2, (mouse_randomx, mouse_randomy))

    if (mouse_randomx < 250 and (mouse_randomy > 200 and mouse_randomy < 318)) or mouse_randomx > 630 or mouse_randomy < 200 or mouse_randomy > 570:
        game_over()
        exit = True
    if (mouse_randomx < 250 and mouse_randomy > 420):
        game_over()
        exit = True
    if (mouse_random == cat_random):
        game_over()
        exit = True
    elif mouse_randomx < 200 and (mouse_randomy < 420 and mouse_randomy > 300):
        win.fill(BLACK)
        wins = pygame.image.load('wins.png')
        win.blit(wins, (50, 100))
        sound_obj = pygame.mixer.Sound('winning.mp3')
        sound_obj.play()
        time.sleep(2)
        sound_obj.stop()
        exit = True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit = True
