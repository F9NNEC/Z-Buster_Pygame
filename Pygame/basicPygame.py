import pygame
import random

# initialize the pygame
pygame.init()

# create screen, tittle and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fennec")

icon = pygame.image.load('fnnc.png')
pygame.display.set_icon(icon)


# player
adit = pygame.image.load('char.png')
playerX = 368
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(adit, (x, y))

# enemy
alien = pygame.image.load('alien.png')
enemyX = random.randint(10,790)
enemyY = 100
enemyX_change = 0

def enemy(x, y):
    screen.blit(alien, (x, y))

# game loop
running = True
while running:
    # window color red, green, blue
    screen.fill((0, 0, 0))

    # exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

    # if keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    # make the player move
    playerX += playerX_change

    # check if character touch edges
    if playerX <= 1:
        playerX_change = 0
    elif playerX >= 736:
        playerX_change = 0

    # make player appear to window
    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()