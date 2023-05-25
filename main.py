import pygame
import random
from time import sleep
pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Aquarium")

Mood = pygame.image.load('Moods.png') #load your spritesheet
Mood.set_colorkey((255,0,255))

Goldy = pygame.image.load('Goldfish.png')
Goldy.set_colorkey((255, 0, 255))

Pinky = pygame.image.load('Pinkfish.png')
Pinky.set_colorkey((255, 255, 255))

Plant = pygame.image.load('Plant.png')
Plant.set_colorkey((255,255,255))

Tall = pygame.image.load('Tall.png')
Tall.set_colorkey((255,255,255))

rock = pygame.image.load('rock.png')
rock.set_colorkey((255, 255, 255))

broom = pygame.image.load('Broom.png')
broom.set_colorkey((255, 255, 255))

flakes = pygame.image.load('Flakes.png')
flakes.set_colorkey((255, 255, 0))


gruigi = pygame.image.load('gruigi.jpg')
gruigi.set_colorkey((255,255,255))
Gwidth = 293
Gheight = 500

frameWidth = 100
frameHeight = 100
RowNum = 0
frameNum = 0

Width = 100
Height = 100
RowN = 0
frameN = 0

FframeWidth = 20
FframeHeight = 20
FRowNum = 0
FframeNum = 0

F2frameWidth = 20
F2frameHeight = 20
F2RowNum = 0
F2frameNum = 1

plantWidth = 75
plantHeight = 75
PRowNum = 0
PframeNum = 0

tallWidth = 75
tallHeight = 120
TRowNum = 0
TframeNum = 0

rockWidth = 75
rockHeight = 75
RRowNum = 0
RframeNum = 0

fx = 350
fy = 250
fVx = 2
fVy = 2

fx2 = 300
fy2 = 200
fVx2 = -4
fVy2 = 2

gx = 0
gxpos = -293

color = (255, 137, 0)
color2 = (220, 12, 100)

clock = pygame.time.Clock()
doExit = False
D = 200
w = 200
tank = (0, 0, 255)

score = 0
bruh = False

ticker = 0

while not doExit:

    clock.tick(60)
    event = pygame.event.wait(10)
    xpos = 0
    ypos = 0
    ticker += 1
    if ticker % 100 == 0:
        score += 1
        ticker = 0
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
    if fx < 60:
        FframeNum = 0
        fVx *= -1
    if fx + 20 > 640:
        FframeNum = 1
        fVx *= -1
    if fy < 100 or fy + 20 > 440:
        fVy *= -1

    if fx2 < 60:
        F2frameNum = 0
        fVx2 *= -1
    if fx2 + 20 > 640:
        F2frameNum = 1
        fVx2 *= -1
    if fy2 < 100 or fy2 + 20 > 440:
        fVy2 *= -1
    if w >= 200:
        w = 200
    if w < 0:
      w = 0
    if w < 25:
      FRowNum = 1
      F2RowNum = 1
      color = (200,200,200)
      color2 = (200,200,200)
      
        
    else:
      color = (255, 137, 0)
      color2 = (220, 12, 100)
    if mousePos[0] > 0 and mousePos[0] < 100 and mousePos[1] > 400 and mousePos[1] < 500:
        print("clean")
        D += 20
       
    else:
        D -= .1
        
    if mousePos[0] > 0 and mousePos[0] < 10 and mousePos[1] > 0 and mousePos[1] < 10:
        bruh = True
    else:
        bruh = False
        
        
        
    if D <= 120:
        RowNum = 1
        tank = (0, 70, 140)
    if D <= 90:
        RowNum = 2
        tank = (0, 140, 110)
    if D <= 50:
        RowNum = 3
        tank = (0, 210, 40)
    if D <= 20 and w is not 0:
        w -= .2
        RowNum = 4
    if D > 120:
        RowNum = 0
        tank = (0,0,255)
    if D > 200:
        D = 200
    if D < 0:
      D = 0
    
    
    if w == 0:
      fVy -= .01
      fVy2 -= .01
      fVx = 0
      fVx2 = 0
      if fy <= 120 and fy2 <= 120:
        doExit = True
    fx += fVx
    fy += fVy
    fx2 += fVx2
    fy2 += fVy2
    gxpos += gx
    screen.fill((51, 42, 100))
    #Fish drawn to the screen
    screen.blit(rock, (175,375), (rockWidth*RframeNum, RRowNum*rockHeight,rockWidth, rockHeight))

    screen.blit(Plant,(400, 365), (plantWidth*PframeNum, PRowNum*plantHeight, plantWidth, plantHeight))
    screen.blit(Plant,(100, 365), (plantWidth*PframeNum, PRowNum*plantHeight, plantWidth, plantHeight))
    screen.blit(Tall,(350, 320), (tallWidth*TframeNum, TRowNum*tallHeight, tallWidth, tallHeight))
    

    screen.blit(rock, (460,375), (rockWidth*RframeNum, RRowNum*rockHeight,rockWidth, rockHeight))

    screen.blit(Goldy, (fx, fy), (FframeWidth*FframeNum, FRowNum*FframeHeight, FframeWidth, FframeHeight))
    screen.blit(Pinky, (fx2, fy2), (F2frameWidth*F2frameNum, F2RowNum*F2frameHeight, F2frameWidth, F2frameHeight))
    screen.blit(Plant, (250, 365), (plantWidth*PframeNum, PRowNum*plantHeight, plantWidth, plantHeight))
    screen.blit(rock, (275,375), (rockWidth*RframeNum, RRowNum*rockHeight,rockWidth, rockHeight))
    screen.blit(Tall, (520, 320), (tallWidth*TframeNum, TRowNum*tallHeight, tallWidth, tallHeight))
    
    #transparent water
    s = pygame.Surface((600, 350))  # the size of your rect
    s.set_alpha(75)  # alpha level
    s.fill((tank))  # this fills the entire surface
    screen.blit(s, (50, 100))  # (0,0) are the top-left coordinates

    #checks if red button is being pressed and will feed the fish
    if mousePos[0] > 600 and mousePos[0] < 700 and mousePos[1] > 400 and mousePos[1] < 500 and w <= 200:
        print("fed")
        w += 50
        for i in range(5):
            x = random.randrange(50, 640)
            y = random.randrange(100, 140)
            pygame.draw.rect(screen, (200, 150, 0), (x, y, 10, 10))
    else:
        w -= .1
    

    pygame.draw.rect(screen, (105, 56, 0), (40, 450, 620, 100))
    pygame.draw.rect(screen, (85, 36, 0), (40, 450, 620, 100), 5)
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 600, 400), 10)
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 600, 400), 5)
    pygame.draw.rect(screen, (0, 0, 0), (45, 50, 610, 25))
    
    screen.blit(Mood, (600, 0), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    
    pygame.draw.circle(screen, (255, 0, 0), (650, 450), 50)
    pygame.draw.circle(screen, (0, 0, 255), (50, 450), 50)
    
    screen.blit(broom, (0, 400), (Width*frameN, RowN*Height, Width, Height))
    screen.blit(flakes, (600, 390), (Width*frameN, RowN*Height, Width, Height))
    if bruh == True:
        screen.blit(gruigi, (250, 0), (Gwidth*frameN, RowN*Gheight, Gwidth, Gheight))


    pygame.draw.rect(screen, (0, 0, 0), (10, 20, 200, 20))
    pygame.draw.rect(screen, (255, 0, 0), (10, 20, w, 20))
    
    pygame.draw.rect(screen, (0, 0, 0), (10, 50, 200, 20))
    pygame.draw.rect(screen, (0, 0, 255), (10, 50, D, 20))
    font = pygame.font.Font(None, 65)
    text = font.render(str(score),1, (255,255,255))
    screen.blit(text, (390,25))
    text = font.render(str("Score: "),1, (255,255,255))
    screen.blit(text, (250,25))
    
    
    pygame.display.flip()
  
pygame.quit()
