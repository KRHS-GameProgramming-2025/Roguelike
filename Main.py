import pygame, sys, math, random
from Hud import *
from Enemy import *
from Character import *
from Tile import *

pygame.init()
clock = pygame.time.Clock();
size= [(220*6), (150*6)]
screen = pygame.display.set_mode(size)

mode="start"

while True:
    bg=pygame.image.load('Screen/startScreen.png')
    bg=pygame.transform.scale(bg, size)
    pygame.mixer.music.load('Sound/Music/breaking_bud.mp3')
    pygame.mixer.music.play(-1,3.5,0)
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
    bg=pygame.transform.scale(bg, size)
    pygame.mixer.music.load('Sound/Music/roguelike_loop_1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1,0,0)
    
    player = baseCharacter("Sprite" + "/" + "Player" + "/" + "100x100_Walt" + "/" + "Walter", 6, [800, 500], "player")
    
    enemy = Enemy("Sprite" + "/" + "Placeholders" + "/" + "placeholder", 3, [50, 50],)
    
    projectiles = []
    mousePos = [0,0]

    while mode=="play":
        
        
        if player.living==False:
            mode="game over"
        
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
                elif event.key == pygame.K_l:
                    player.health(-10)
                    print(player.hp)
                elif event.key == pygame.K_k:
                    player.health(10)
                    print(player.hp)
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.goKey("sLeft")
                elif event.key == pygame.K_d:
                    player.goKey("sRight")
                elif event.key == pygame.K_w:
                    player.goKey("sUp")
                elif event.key == pygame.K_s:
                    player.goKey("sDown")
            
            elif event.type == pygame.MOUSEMOTION:
                mousePos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    projectiles += [player.fire(event.pos)]
                mousePos = event.pos
                
    
        player.move()
        player.aim(mousePos)
        player.wallCollide(size)
        
        print(len(projectiles))
        for p in projectiles: 
            p.move()
            if p.wallCollide(size):
                projectiles.remove(p)
        
        enemy.move(player.rect.center)
        
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        for p in projectiles: 
            screen.blit(p.image, p.rect)
        screen.blit(player.image,player.rect)
        screen.blit(enemy.image,enemy.rect)
        pygame.display.flip()
        clock.tick(60)

    bg=pygame.image.load('Screen/endScreen.png')     
    bg=pygame.transform.scale(bg, size)
    pygame.mixer.music.load('Sound/SFX/gong.mp3')
    pygame.mixer.music.play(-1,0,0)
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
             
          
