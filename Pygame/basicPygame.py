import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# create screen, tittle and icon
screen = pygame.display.set_mode((480, 854))
pygame.display.set_caption("Fennec - Z Buster")

icon = pygame.image.load('fnnc.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('dirt.png')
tree = pygame.image.load('tree.png')

# player
adit = pygame.image.load('mainChar.png')
playerX = 176 # (screen width / 2) - (player width / 2)
playerY = 700
playerX_change = 0

def player(x, y):
    screen.blit(adit, (x, y))

# enemy
alien = []
enemyX = []
enemyY = []
enemyY_change = []
numOfEnemies = 6

for i in range(numOfEnemies):
    alien.append(pygame.image.load('zombie.png')) # append - store to []
    enemyX.append(random.randint(0,352))
    enemyY.append(random.randint(0,40))
    enemyY_change.append(random.randint(1, 3))

def enemy(x, y, i):
    screen.blit(alien[i], (x, y))

# bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 700
bulletY_change = 30
bullet_state = 'ready'

def fire_bullet(x, y): # set bullet state and possition
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 46, y - 20))

# collision and calculate distance between enemy and bullet
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False

# score
score_value = 0
scoreFont = pygame.font.Font('freesansbold.ttf', 16)
scoreX = 30
scoreY = 30

def showScore(x, y):
    score = scoreFont.render('Score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# background sound
mixer.music.load('backgroundMusic.wav')
mixer.music.play(-1) #-1 for play loop
mixer.music.set_volume(0.5)

# game Over text
score_value = 0
GOverFont = pygame.font.Font('freesansbold.ttf', 50)

def gameOverText():
    GOText = GOverFont.render('Game Over', True, (255, 69, 69))
    screen.blit(GOText, (100, 400))

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
                bulletSound = mixer.Sound('gun.wav')
                bulletSound.play()
                bulletSound.set_volume(0.8)

    # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5

            if event.key == pygame.K_d:
                playerX_change = 5

    # if keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
        
    # make the player move
    playerX += playerX_change

    # check if character touch edges
    if playerX <= 1:
        playerX = 1
    elif playerX >= 416:
        playerX = 416
    for i in range(numOfEnemies):
        # make the enemy move
        enemyY[i] += enemyY_change[i]

        # check collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 700
            bullet_state = 'ready'
            score_value += 1
            hitSound = mixer.Sound('explosion.wav')
            hitSound.play()
            hitSound.set_volume(0.3)
            
            # respawn enemy on random poss
            enemyX[i] = random.randint(0,352)
            enemyY[i] = random.randint(0,40)
            

        # gameOver
        if enemyY[i] >= 580:
            enemyY_change[i] = 0
            bulletX = -100
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('close the game and re-run the code to play again:)')
            gameOverText()
            bulletSound.stop()
            mixer.music.stop()

            scoreX = 200
            scoreY = 450
        
        # make enemy appear to window
        enemy(enemyX[i], enemyY[i], i)


        # make player appear to window
        player(playerX, playerY)

    # check if bullet touching edges
    if bulletY <= 0:
        bulletY = 700
        bullet_state = 'ready'

    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    # tree
    screen.blit(tree, (0, 0))

    showScore(scoreX, scoreY)
    pygame.display.update()