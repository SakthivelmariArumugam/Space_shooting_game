import pygame

import math

import random

from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

background=pygame.image.load('space.jpg')

mixer.music.load('powerful.mp3')

mixer.music.play(-1)

space_new_width=800

space_new_height=600

space_resize_image=pygame.transform.scale(background,(space_new_width,space_new_height))

bullet=pygame.image.load('bullet.png')

bullet_new_width=32

bullet_new_height=32

bullet_resize_image=pygame.transform.scale(bullet,(bullet_new_width,bullet_new_height))

bulletX=0

bulletY=480

bulletX_change=0

bulletY_change=3

bullet_state="ready"

score_value=0

font=pygame.font.Font('freesansbold.ttf',32)

textX=10

textY=10

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):

    score=font.render("Score:"+str(score_value),True,(255,255,255))

    screen.blit(score,(x,y))

def game_over_text():

    over_text=over_font.render("GAME OVER",True,(255,255,255))

    screen.blit(over_text,(200,250))

pygame.display.set_caption("Space Invaders")

icon=pygame.image.load('ufo.png')

pygame.display.set_icon(icon)

playerImg=pygame.image.load('spaceship.png')

new_width=64

new_height=64

resized_image=pygame.transform.scale(playerImg,(new_width,new_height))

playerX=370

playerY=480

playerX_change=0

enemyX=[]

enemyY=[]

enemyX_change=[]

enemyY_change=[]

enemy_resized_image=[]

enemies=['alien.png','alien2.png','alien3.png','alien4.png','monster.png','silly.png']

number_of_enemies=6

for i in range(number_of_enemies):

    enemyImg=pygame.image.load(random.choice(enemies))

    enemy_new_width=64

    enemy_new_height=64

    enemyX.append(random.randint(0,736))

    enemyY.append(random.randint(50,150))

    enemyX_change.append(0.3)

    enemyY_change.append(40)

    enemy_resized_image.append(pygame.transform.scale(enemyImg,(enemy_new_width,enemy_new_height)))

score=0

def player(x,y):
    
    screen.blit(resized_image,(x,y))

def enemy(x,y,i):

    screen.blit(enemy_resized_image[i],(x,y))

def fire_bullet(x,y):

    global bullet_state

    bullet_state = "fire"

    screen.blit(bullet_resize_image,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):

    distance =math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))

    if distance<27:

        return True
    else:

        return False

running=True

while running:

    screen.fill((0,0,0))

    screen.blit(space_resize_image,(0,0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            running=False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:

                playerX_change=-0.4
                
            if event.key == pygame.K_RIGHT:

                playerX_change=0.4

            if event.key == pygame.K_SPACE:

                bullet_sound=mixer.Sound('blaster.mp3')

                bullet_sound.play()

                if bullet_state is "ready":

                    bulletX=playerX

                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                playerX_change=0

    playerX+=playerX_change

    if playerX<=0:
        
        playerX=0
        
    elif playerX>=736:
        
        playerX=736

    for i in range(number_of_enemies):

        if enemyY[i]>400:

            for j in range(number_of_enemies):

                enemyY[j]=2000

            game_over_text()

            break

        enemyX[i]+=enemyX_change[i]

        if enemyX[i]<=0:
            
            enemyX_change[i]=0.3

            enemyY[i]+=enemyY_change[i]
            
        elif enemyX[i]>=736:
            
            enemyX_change[i]=-0.3

            enemyY[i]+=enemyY_change[i]

        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)

        if collision:

            expolsion_sound=mixer.Sound('explosion.mp3')

            expolsion_sound.play()

            bulletY=480

            bullet_state="ready"

            score_value+=1

            print(score_value)

            enemyX[i]=random.randint(0,736)

            enemyY[i]=random.randint(50,150)
        
        enemy(enemyX[i],enemyY[i],i)
  

    if bulletY<=0:
        
        bulletY = 480

        bullet_state = "ready"

    if bullet_state is "fire":

        fire_bullet(bulletX,bulletY)

        bulletY -= bulletY_change

   
        
    player(playerX,playerY)

    show_score(textX,textY)
  
    pygame.display.update()
