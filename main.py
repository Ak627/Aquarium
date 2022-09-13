import pygame
import random

pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Aquarium")

Mood = pygame.image.load('Moods.png') #load your spritesheet
Mood.set_colorkey((255,0,255))

frameWidth = 100
frameHeight = 100
RowNum = 0
frameNum = 0

fx = 350
fy = 250
fVx = 2
fVy = 2

fx2 = 300
fy2 = 200
fVx2 = -4
fVy2 = 2

color = (255, 137, 0)
color2 = (220, 12, 100)

clock = pygame.time.Clock()
doExit = False
D = 200
w = 200
tank = (0, 0, 255)
while not doExit:

    clock.tick(60)
    event = pygame.event.wait(10)
    xpos = 0
    ypos = 0
    mousePos = (xpos, ypos)

    #Input Section---------------------------------------------------------
    if event.type == pygame.MOUSEBUTTONDOWN:  #CLICK
        mousePos = event.pos

    if event.type == pygame.MOUSEBUTTONUP:
        draw = False

#       if event.type == pygame.MOUSEMOTION:
#             mousePos = event.pos

    if event.type == pygame.QUIT:  #close game window
        break

    if w > 200:
        w = 200
    if fx < 60 or fx + 20 > 640:
        fVx *= -1
    if fy < 100 or fy + 20 > 440:
        fVy *= -1

    if fx2 < 60 or fx2 + 20 > 640:
        fVx2 *= -1
    if fy2 < 100 or fy2 + 20 > 440:
        fVy2 *= -1

    fx += fVx
    fy += fVy
    fx2 += fVx2
    fy2 += fVy2
    if w == 0:
      fVy -= .01
      fVy2 -= .01
      if fy and fy2 <= 100:
        doExit = True
    screen.fill((51, 42, 100))
    #Fish drawn to the screen
    pygame.draw.rect(screen, (color), (fx, fy, 20, 20))
    pygame.draw.rect(screen, (color2), (fx2, fy2, 20, 20))
    #transparent water
    s = pygame.Surface((600, 350))  # the size of your rect
    s.set_alpha(75)  # alpha level
    s.fill((tank))  # this fills the entire surface
    screen.blit(s, (50, 100))  # (0,0) are the top-left coordinates

    #checks if red button is being pressed and will feed the fish

    if mousePos[0] > 600 and mousePos[0] < 700 and mousePos[
            1] > 400 and mousePos[1] < 500:
        print("fed")
        w += 50
        for i in range(5):
            x = random.randrange(50, 640)
            y = random.randrange(100, 140)
            pygame.draw.rect(screen, (200, 150, 0), (x, y, 10, 10))
    else:
        w -= .1
    if w > 200:
        w = 200
    if w < 0:
      w = 0
    if w < 25:
      color = (200,200,200)
      color2 = (200,200,200)
      
        
    else:
      color = (255, 137, 0)
      color2 = (220, 12, 100)
    if mousePos[0] > 0 and mousePos[0] < 100 and mousePos[
            1] > 400 and mousePos[1] < 500:
        print("clean")
        D += 20
       
    else:
        D -= .1
    if D <= 120:
        RowNum = 1
        tank = (0, 70, 140)
    if D <= 90:
        RowNum = 2
        tank = (0, 140, 110)
    if D <= 50:
        RowNum = 3
        tank = (0, 210, 40)
    if D <= 20:
        w -= .2
        RowNum = 4
    if D > 120:
        RowNum = 0
        tank = (0,0,255)
    if D > 200:
        D = 200
    if D < 0:
      D = 0
    if D == 0:
        w -= .3

    pygame.draw.rect(screen, (105, 56, 0), (40, 450, 620, 100))
    pygame.draw.rect(screen, (85, 36, 0), (40, 450, 620, 100), 5)
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 600, 400), 10)
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 600, 400), 5)
    pygame.draw.rect(screen, (0, 0, 0), (45, 50, 610, 25))
    
    screen.blit(Mood, (600, 0), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    
    pygame.draw.circle(screen, (255, 0, 0), (650, 450), 50)
    pygame.draw.circle(screen, (0, 0, 255), (50, 450), 50)
    pygame.draw.rect(screen, (0, 0, 0), (10, 20, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 20, w, 20))
    pygame.draw.rect(screen, (0, 0, 0), (10, 50, 200, 20))
    pygame.draw.rect(screen, (255, 255, 0), (10, 50, D, 20))
    pygame.display.flip()
  
pygame.quit()
