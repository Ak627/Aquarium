import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Aquarium")

fx = 350
fy = 250
fVx = 2
fVy = 2

fx2 = 300
fy2 = 200
fVx2 = -4
fVy2 = 2
clock = pygame.time.Clock()
doExit = False
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
w = 200
while not doExit:
  clock.tick(60)
  event = pygame.event.wait()    


#Input Section---------------------------------------------------------
  if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
        mousePos = event.pos


  if event.type == pygame.QUIT: #close game window
        break
  if mousePos[0] > 600 and mousePos[0] < 700 and mousePos[1] > 400 and mousePos[1] < 500:
        print("fed")
        w += 50
    
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
  w -=  .1

  screen.fill((51, 42, 100))
  s = pygame.Surface((600,350))  # the size of your rect
  s.set_alpha(75)                # alpha level
  s.fill((0,0,255))           # this fills the entire surface
  screen.blit(s, (50,100))    # (0,0) are the top-left coordinates
  pygame.draw.rect(screen, (105,56,0), (40, 450, 620, 100))
  pygame.draw.rect(screen, (85,36,0), (40, 450, 620, 100), 5)
  pygame.draw.rect(screen, (255, 255, 255), (50, 50, 600, 400), 10)
  pygame.draw.rect(screen, (0,0,0), (50, 50, 600, 400), 5)
  pygame.draw.rect(screen, (0,0,0), (45, 50, 610, 25))
  pygame.draw.rect(screen, (255, 137, 0), (fx, fy, 20, 20))
  pygame.draw.rect(screen, (220, 12, 100), (fx2, fy2, 20, 20))
  
  pygame.draw.rect(screen, (255,255,255), (600, 400, 100, 100),5)
  pygame.draw.circle(screen, (255, 0, 0), (650, 450), 50)
  pygame.draw.rect(screen, (0, 0, 0), (10, 20, 200, 20))
  pygame.draw.rect(screen, (0, 255, 0), (10, 20, w, 20))
  


  pygame.display.flip()
pygame.quit()
