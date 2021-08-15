import pygame
import time
import random
from random import randrange
from random import randint
YELLOW = (255, 228, 196)
BLUE = (30, 144, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 117.6
HEIGHT = 117.6
MARGIN = 3
x = randrange(250, 630, 118)
y = randrange(200, 570, 118)
pos_x = randrange(230, 600, 118)
pos_y = randrange(195, 550, 118)
grid = []
for row in range(6):
    grid.append([])
    for column in range(6):
        grid[row].append(0)
grid[1][0] = 1
grid[1][1] = 0
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.init()
win = pygame.display.set_mode((900, 800))
win.fill(YELLOW)
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
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * (column + 1.82) + MARGIN,
                              (MARGIN + HEIGHT) * (row + 1.4) + MARGIN,
                              WIDTH,
                              HEIGHT])
image2 = pygame.image.load('Image/mouse.png')
win.blit(image2, (x, y))
image = pygame.image.load('Image/cat2.png')
win.blit(image, (120, 120))
pygame.display.update()
List_of_movement = [(0, -118), (0, 118), (118, 0), (-118, 0)]

exit = False
while not exit:
    pygame.draw.rect(win, BLACK, [102, 52, 718, 718])
    background_blue()
    background_green()
    image = pygame.image.load('Image/cat2.png')
    win.blit(image, (pos_x, pos_y))
    image2 = pygame.image.load('Image/mouse.png')
    win.blit(image2, (x, y))
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit = True
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            x += WIDTH
        if key[pygame.K_LEFT]:
            x -= WIDTH
        if key[pygame.K_UP]:
            y -= HEIGHT
        if key[pygame.K_DOWN]:
            y += HEIGHT
while True:
    if x < 250 or x > 630 or y < 200 or y > 570:
        time.sleep(1)
        Game_over = pygame.image.load('Image/over.png')
        win.fill(BLACK)
        win.blit(Game_over, (50, 100))
    elif grid[row][column] == 0:
        time.sleep(1)
        win = pygame.image.load('Image/win.jpg')
        win.blit(win, (50, 100))