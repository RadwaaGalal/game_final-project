import pygame
YELLOW = (255, 228, 196)
BLUE = (30, 144, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 117.6
HEIGHT = 117.6
MARGIN = 3
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)
grid[0][0] = 1
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.init()
win = pygame.display.set_mode((900, 800))
win.fill(YELLOW)
pygame.draw.rect(win, BLUE, [75, 25, 750, 750])
pygame.draw.rect(win, BLACK, [75, 25, 750, 750])
for row in range(6):
    for column in range(5):
        color = BLUE
        if grid[row][column] == 1:
            color = BLUE
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * (column + 0.6) + MARGIN,
                          (MARGIN + HEIGHT) * (row + 0.19) + MARGIN,
                          WIDTH,
                          HEIGHT])
image = pygame.image.load('Image/cat2.png')
win.blit(image, (110, 110))
image = pygame.image.load('Image/mouse.png')
win.blit(image, (220, 220))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def background_green():
    for row in range(5):
        for column in range(5):
            color = GREEN
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * (column + 0.81) + MARGIN,
                              (MARGIN + HEIGHT) * (row + 0.81) + MARGIN,
                              WIDTH,
                              HEIGHT])

x = 110
y = 110
image = pygame.image.load('Image/cat2.png')
win.blit(image, (x, y))
image = pygame.image.load('Image/mouse.png')
win.blit(image, (220, 220))
position = image.get_rect()
for x in range(100):
    position = position.move(2, 0)
    image = pygame.image.load('Image/cat2.png')
    pygame.display.update()
    pygame.time.delay(100)

pygame.display.update()
exit = False
while not exit:
    pygame.draw.rect(win, BLACK, [100, 100, 600, 600])
    background_green()
    image = pygame.image.load('Image/mouse.png')
    win.blit(image, (x, y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit = True
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            x += 130
        if key[pygame.K_LEFT]:
            x -= 130
        if key[pygame.K_UP]:
            y -= 130
        if key[pygame.K_DOWN]:
            y += 130