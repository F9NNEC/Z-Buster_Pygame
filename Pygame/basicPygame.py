import pygame
import random

# initialize the pygame
pygame.init()

# create screen, tittle and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fennec")

icon = pygame.image.load('fnnc.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('spaceBackground.png')


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
enemyY = 50
enemyX_change = 2
enemyY_change = 40

def enemy(x, y):
    screen.blit(alien, (x, y))

# game loop
running = True
while running:
    # window color red, green, blue
    screen.fill((0, 0, 0))

    # background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
    # exit button
        if event.type == pygame.QUIT:
            running = False
    
    # check if mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Pressed')
        if event.type == pygame.MOUSEBUTTONUP:
            print('Released')

    # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -4

            if event.key == pygame.K_d:
                playerX_change = 4


    # if keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
        
    # make the player move
    playerX += playerX_change

    # check if character touch edges
    if playerX <= 1:
        playerX = 1
    elif playerX >= 736:
        playerX = 736

    # make the enemy move
    enemyX += enemyX_change

    # check if enemy touch edges
    if enemyX <= 1:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # make player appear to window
    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()