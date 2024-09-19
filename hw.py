import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1250,690))

mushroom = pygame.image.load("lesson 5/picture/mushroom alive.png")
bg = pygame.image.load("lesson 5/picture/mushroom bg.jpg")
bg = pygame.transform.scale(bg,(1250,690))

mushx = 625
mushy = 345

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                mushy -= 20
             if event.key == pygame.K_s:
                mushy += 5
             if event.key == pygame.K_a:
                mushx -= 5
             if event.key == pygame.K_d:
                mushx += 5
    
    screen.blit(bg,(0,0))
    screen.blit(mushroom,(mushx,mushy))

    pygame.display.update()
