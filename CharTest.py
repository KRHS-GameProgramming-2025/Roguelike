import pygame, sys, math, random

from Character import *

pygame.init()
clock = pygame.time.Clock();
size= [1800, 1000]
screen = pygame.display.set_mode(size)

bg=pygame.image.load('Screen/BackGround.png')
player = baseCharacter("Sprite/Player/Walt/Walter", 5, [900,500], "player")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
        if event.type == pygame.MOUSEMOTION:
            player.aim(event.pos)
            
    player.move()
    player.wallCollide(size)
    
    screen.fill((97, 164, 229))
    screen.blit(bg,[0,0])
    screen.blit(player.image,player.rect)
    pygame.display.flip()
    clock.tick(70)
