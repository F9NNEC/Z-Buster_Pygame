import pygame
import random
import math
from pygame import mixer

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
alien = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnemies = 5

for i in range(numOfEnemies):
    alien.append(pygame.image.load('alien.png')) # append - store to []
    enemyX.append(random.randint(10,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(alien[i], (x, y))

# bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 20
bullet_state = 'ready'

def fire_bullet(x, y): # set bullet state and possition
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y - 20))

# collision and calculate distance between enemy and bullet
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# score
score_value = 0
scoreFont = pygame.font.Font('freesansbold.ttf', 16)
scoreX = 10
scoreY = 10

def showScore(x, y):
    score = scoreFont.render('score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# background sound
mixer.music.load('backgroundMusic.wav')
mixer.music.play(-1) #-1 for play loop




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
    
    # check if mouse click fire bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bullet_state is 'ready': #only shoot when bullet is ready
                bulletX = playerX
                fire_bullet(bulletX, playerY)
                bulletSound = mixer.Sound('laser.wav')
                bulletSound.play()

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

    for i in range(numOfEnemies):
        # make the enemy move
        enemyX[i] += enemyX_change[i]

        # check if enemy touch edges
        if enemyX[i] <= 1:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # check collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            hitSound = mixer.Sound('explosion.wav')
            hitSound.play()
            

            # respawn enemy on random poss
            enemyX[i] = random.randint(10,735)
            enemyY[i] = random.randint(50,150)

        # make enemy appear to window
        enemy(enemyX[i], enemyY[i], i)

        # make player appear to window
        player(playerX, playerY)



    # check if bullet touching edges
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    showScore(scoreX, scoreY)
    pygame.display.update()