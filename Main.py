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


    
    player = baseCharacter("Sprite/Placeholders/placeholder.png", 5, [0, 0], "player")

    while mode=="play":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="game over"
                if event.key == pygame.K_a:
                    player.goKey("left")
                elif event.key == pygame.K_d:
                    player.goKey("right")
                elif event.key == pygame.K_w:
                    player.goKey("up")
                elif event.key == pygame.K_s:
                    player.goKey("down")
                    
                                #Directionals
                                
                elif event.key == pygame.K_LEFT:
                    player.aim("left")
                elif event.key == pygame.K_RIGHT:
                    player.aim("right")
                elif event.key == pygame.K_UP:
                    player.aim("up")
                elif event.key == pygame.K_DOWN:
                    player.aim("down")
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.goKey("sLeft")
                elif event.key == pygame.K_d:
                    player.goKey("sRight")
                elif event.key == pygame.K_w:
                    player.goKey("sUp")
                elif event.key == pygame.K_s:
                    player.goKey("sDown")
                    
                elif event.key == pygame.K_LEFT:
                    player.aim("sLeft")
                elif event.key == pygame.K_RIGHT:
                    player.aim("sRight")
                elif event.key == pygame.K_UP:
                    player.aim("sUp")
                elif event.key == pygame.K_DOWN:
                    player.aim("sDown")
        
        player.move()
        
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        screen.blit(player.image,player.rect)
        pygame.display.flip()
        clock.tick(70)

    bg=pygame.image.load('Screen/END.png')     

    while mode=="game over":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="start"
                
              
                    
                    
            screen.fill((97, 164, 229))
            screen.blit(bg,[0,0])
            pygame.display.flip()
             
          
