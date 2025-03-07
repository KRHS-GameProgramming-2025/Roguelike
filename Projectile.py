import pygame, sys, math

class Bullet():
    def __init__(self,owner, speed, startPos=[0,0]):
        self.image = pygame.image.load( "Bullet/Bullet.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.size = (self.rect.height/10 + self.rect.width/10)/2
    
        self.rect = self.rect.move(startPos)
        self.rad = (self.rect.height/50 + self.rect.width/50)/50
        
        self.owner=owner
        self.kind="bullet"

    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.right < 0:
            return True
        if self.rect.bottom < 0:
            return True
        if self.rect.left > width:
            return True
        if self.rect.top > height:
            return True
        
        return False
        
       
    
    def shipCollide(self,ship):
        if self.owner !=ship.kind:
            if ship.rect.left <= self.rect.right:
                if ship.rect.right >= self.rect.left:
                    if ship.rect.top <= self.rect.bottom:
                        if ship.rect.bottom >= self.rect.top:
                            print('collison')
                            return True
        return False
        
    def bulletCollide(self,ship):
        if self.owner !=ship.owner:
            if ship.rect.left <= self.rect.right:
                if ship.rect.right >= self.rect.left:
                    if ship.rect.top <= self.rect.bottom:
                        if ship.rect.bottom >= self.rect.top:
                            print('collison wall hit')
                            return True
        return False
        
    def die(self):
        pass
#projectile
