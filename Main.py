import pygame, sys, math, random
from Hud import *
from Enemy import *
from MiniBossEnemy import *
from Character import *
from Tile import *

pygame.init()
clock = pygame.time.Clock();
size=[(100*19), (100*10)]
screen = pygame.display.set_mode(size)

mode="start"

while True:
    bg=pygame.image.load('Screen/startScreen.png')
    bg=pygame.transform.scale(bg, size)
    pygame.mixer.music.load('Sound/Music/bring_it_brah.mp3')
    pygame.mixer.music.play(-1,0,0)
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                     mode="play"
            
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.mixer.music.load('Sound/Music/roguelike_loop_1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1,0,0)
    
    try:
        player = baseCharacter("Sprite" + "/" + "Player" + "/" + "100x100_Walt" + "/" + "Walter", 6, [800, 500], "player")
    except:
        player = baseCharacter("Sprite" + "/" + "Placeholders" + "/" + "Player" + "/" + "placeholder", 6, [800, 500], "player")
     
    enemies = []
    #Enemy("Sprite" + "/" + "Placeholders" + "/" + "placeholder", 3, [50, 50],),
    #Enemy("Sprite" + "/" + "Placeholders" + "/" + "placeholder", 3, [300, 300],)]
    numEnemies = 0
    numMiniBossEnemies = 0

    numWave = 0
    damage = 20
    
    projectiles = []
    mousePos = [0,0]
    
    wave = Hud("Wave: ",numWave,[0,0])

    while mode=="play":
        
        
        if player.living==False:
            mode="game over"
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
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
        
        if numWave <= 5:
            bg=pygame.image.load('Screen/BackGround.png')
            bg=pygame.transform.scale(bg, size)
            
        elif numWave > 5 and numWave < 20:
                bg=pygame.image.load('Screen/BackGround2.png')
                bg=pygame.transform.scale(bg, size)
                
        elif numWave > 20:
                bg=pygame.image.load('Screen/BackGround3.png')
                bg=pygame.transform.scale(bg, size)
        
        if len(enemies)==0:
            numWave += 1
            wave.update(numWave)
            if numWave % 5 != 0:
                damage += 10
                numEnemies += 2
                for i in range(random.randint(numEnemies // 2,numEnemies)):
                    side = random.randint(0,3)
                    if side == 0:
                        loc = [random.randint(0, size[0]), 0]
                    elif side == 1:
                        loc = [random.randint(0, size[0]), size[1]]
                    elif side == 2:
                        loc = [0, random.randint(0, size[1])]
                    elif side == 3:
                        loc = [size[0],random.randint(0, size[1])]
                    e = random.randint(0,5)
                    if e == 0:
                        enemies += [Enemy("Enemy" + "/" + "lirili_larila.png", 1, loc)]
                    elif e == 1:
                        enemies += [Enemy("Enemy" + "/" + "tralalero_tralalaDown.png", 2, loc)]
                    elif e == 2:
                        enemies += [Enemy("Enemy" + "/" + "pixil-frame-0 (40).png", 2, loc)]
                    elif e == 3:
                        enemies += [Enemy("Enemy" + "/" + "Chiyo-chichi.png", 3, loc)]
                    elif e == 4:
                        enemies += [Enemy("Enemy" + "/" + "pixil-frame-0 (46).png", 2, loc)]
                    else:
                        enemies += [Enemy("Enemy" + "/" + "troll.png", 2, loc)]
                    
                   
            else: 
                numMiniBossEnemies += 1
                for i in range(numMiniBossEnemies):
                    side = random.randint(0,3)
                    if side == 0:
                        loc = [random.randint(0, size[0]), 0]
                    elif side == 1:
                        loc = [random.randint(0, size[0]), size[1]]
                    elif side == 2:
                        loc = [0, random.randint(0, size[1])]
                    elif side == 3:
                        loc = [size[0],random.randint(0, size[1])]
                    enemies += [MiniBossEnemy("Enemy" + "/" + "Boss" + "/" + "Boss" , 3, loc)]
                
        player.update(mousePos, size)
       
        
        for p in projectiles: 
            p.move()
            if p.wallCollide(size):
                projectiles.remove(p)
            for enemy in enemies:
                if p.enemyCollide(enemy):
                    enemy.projectileCollide(p,damage)
                    projectiles.remove(p)
                    break
            
        
        for enemy in enemies:
            enemy.move(player.rect.center)
            if player.collide(enemy):
                player.health(-2)
                print("hit: " + str(player.hp))
            if not enemy.living:
                enemies.remove(enemy)
            
                
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        for p in projectiles: 
            screen.blit(p.image, p.rect)
        if player.invincible and player.invincibleTimer %2 == 0:
            pass
        else:
            screen.blit(player.image,player.rect)
        for enemy in enemies:
            screen.blit(enemy.image,enemy.rect)
        screen.blit(wave.image,wave.rect)
        pygame.display.flip()
        clock.tick(60)

    
    bg=pygame.image.load('Screen/endScreen.png')     
    bg=pygame.transform.scale(bg, size)
    pygame.mixer.music.load('Sound/SFX/gong.mp3')
    pygame.mixer.music.play(-1,0,0)
    screen.fill((97, 164, 229))
    screen.blit(bg,[0,0])
    pygame.display.flip()
    clock.tick(60)
    
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
             
          
