import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))

fx = 350
fy = 250
fVx = 2
fVy = 2
clock = pygame.time.Clock()
doExit = False

while not doExit:
  clock.tick(60)
  if fx < 60 or fx + 20 > 640:
    fVx *= -1
  if fy < 100 or fy + 20 > 440:
    fVy *= -1
  
  fx += fVx
  fy += fVy
  screen.fill((51, 42, 100))
  s = pygame.Surface((600,350))  # the size of your rect
  s.set_alpha(75)                # alpha level
  s.fill((0,0,255))           # this fills the entire surface
  screen.blit(s, (50,100))    # (0,0) are the top-left coordinates
  pygame.draw.rect(screen, (105,56,0), (40, 450, 620, 100))
  pygame.draw.rect(screen, (255, 255, 255), (50, 50, 600, 400), 10)
  pygame.draw.rect(screen, (0,0,0), (50, 50, 600, 400), 5)
  pygame.draw.rect(screen, (0,0,0), (45, 50, 610, 25))
  pygame.draw.rect(screen, (255, 137, 0), (fx, fy, 20, 20))

  pygame.display.flip()
pygame.quit()
