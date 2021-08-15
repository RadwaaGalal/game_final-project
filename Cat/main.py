import pygame
from random import randrange
'''import pyautogui
import _thread
import time

time.sleep(2)

def kaydir(miktarX, miktarY):
    pyautogui.moveRel(miktarX, miktarY)
    print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        _thread.start_new_thread(kaydir, (1, 1))
        time.sleep(0.08)
except KeyboardInterrupt:
    print('\n')'''
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
        if x == 155 and y == 200:
            print("win")
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
move = randrange(250, 630, 118)
for move in range(20):
    move += WIDTH
    pygame.draw.rect(win, BLACK, [102, 52, 718, 718])
    background_blue()
    background_green()
    image = pygame.image.load('Image/cat2.png')
    win.blit(image, (pos_x, pos_y))
    image2 = pygame.image.load('Image/mouse.png')
    win.blit(image2, (move, move))
    pygame.display.update()
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit = True
