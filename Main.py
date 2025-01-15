import pygame, sys, math, random
from Hud import *
from Enemy import *
from Character import *
from Tile import *

pygame.init()
clock = pygame.time.Clock();
size= [1800, 1000]
screen = pygame.display.set_mode(size)

mode="start"





while True:
    bg=pygame.image.load('Screen/Start.png')
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="play"
            
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        
        pygame.display.flip()
        clock.tick(70)
            
                     
    bg=pygame.image.load('Screen/BackGround.png')







    while mode=="play":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
        
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        
        pygame.display.flip()
        clock.tick(70)
