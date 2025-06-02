import pygame
class Enemy():
    def __init__(self,
                 image,
                 maxSpeed,
                 startPosition = [0, 0],
                 characterType = None):
        # ~ self.imagesUp = [pygame.image.load(image + "Up" + ".png")]
        # ~ self.imagesUpRight = [pygame.image.load(image + "UpRight" + ".png")]
        # ~ self.imagesRight = [pygame.image.load(image + "Right" + ".png")]
        # ~ self.imagesDownRight = [pygame.image.load(image + "DownRight" + ".png")]
        # ~ self.imagesDown = [pygame.image.load(image + "Down" + ".png")]
        # ~ self.imagesDownLeft = [pygame.image.load(image + "DownLeft" + ".png")]
        # ~ self.imagesLeft = [pygame.image.load(image + "Left" + ".png")]
        # ~ self.imagesUpLeft = [pygame.image.load(image + "UpLeft" + ".png")]
        # ~ self.images = self.imagesUp
        # ~ self.frame = 0
        # ~ self.frameMax = len(self.images)-1
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = startPosition)
        
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        
        self.maxSpeed = maxSpeed
        if characterType != None:
            self.kind = characterType
        elif characterType == None:
            self.kind = "None"
        
        self.headingX = "none"
        self.headingY = "none"
        self.pointingX = "none"
        self.pointingY = "up"
        
        self.hp = 100
        self.maxhp = 100
        self.living=True

    def move(self, target):
        self.goTo(target)
        
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def goTo(self, target):
        tx = target[0]
        ty = target[1]
        
        myX = self.rect.centerx
        myY = self.rect.centery
        
        if myX > tx+20:
            self.goKey("left")
            self.aim("left")
        elif myX < tx-20:
            self.goKey("right")
            self.aim("right")
        else:
            self.goKey("sLeft")
            self.aim("sLeft")
            
        if myY > ty+20:
            self.goKey("up")
            self.aim("up")
        elif myY < ty-20:
            self.goKey("down")
            self.aim("down")
        else:
            self.goKey("sUp")
            self.aim("sUp")     
    
    
    
    
    def health(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp=self.maxhp
        if self.hp < 1:
            self.hp=0
            self.living=False
    
    
    
            
    def projectileCollide(self,projectile):
        if projectile.rect.left <= self.rect.right:
            if projectile.rect.right >= self.rect.left:
                if projectile.rect.top <= self.rect.bottom:
                    if projectile.rect.bottom >= self.rect.top:
                        print('collison')
                        self.health(-20)
                        return True
        return False
        
    
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.headingX = "left"
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.headingX = "right"
        elif direction == "up":
            self.speedy = -self.maxSpeed
            self.headingY = "up"
        elif direction == "down":
            self.speedy = self.maxSpeed
            self.headingY = "down"
            
        
        elif direction == "sLeft":
            if self.headingX == "left":
                self.speedx = 0
                self.headingX = "none"
        elif direction == "sRight":
            if self.headingX == "right":
                self.speedx = 0
                self.headingX = "none"
        elif direction == "sUp":
            if self.headingY == "up":
                self.speedy = 0
                self.headingY = "none"
        elif direction == "sDown":
            if self.headingY == "down":
                self.speedy = 0
                self.headingY = "none"
                
    def aim(self, direction):
        if direction == "left":
            self.pointingX = "left"
        elif direction == "right":
            self.pointingX = "right"
        elif direction == "up":
            self.pointingY = "up"
        elif direction == "down":
            self.pointingY = "down"
            
        elif direction == "sLeft":
            if self.pointingX == "left":
                self.pointingX = "none"
        elif direction == "sRight":
            if self.pointingX == "right":
                self.pointingX = "none"
        elif direction == "sUp":
            if self.pointingY == "up":
                self.pointingY = "none"
        elif direction == "sDown":
            if self.pointingY == "down":
                self.pointingY = "none"
                
        # ~ if self.pointingX == "none" and self.pointingY == "up":
            # ~ self.images = self.imagesUp
        # ~ elif self.pointingX == "right" and self.pointingY == "up":
            # ~ self.images = self.imagesUpRight
        # ~ elif self.pointingX == "right" and self.pointingY == "none":
            # ~ self.images = self.imagesRight
        # ~ elif self.pointingX == "right" and self.pointingY == "down":
            # ~ self.images = self.imagesDownRight
        # ~ elif self.pointingX == "none" and self.pointingY == "down":
            # ~ self.images = self.imagesDown
        # ~ elif self.pointingX == "left" and self.pointingY == "down":
            # ~ self.images = self.imagesDownLeft
        # ~ elif self.pointingX == "left" and self.pointingY == "none":
            # ~ self.images = self.imagesLeft
        # ~ elif self.pointingX == "left" and self.pointingY == "up":
            # ~ self.images = self.imagesUpLeft
        
             
        # ~ self.image = self.images[self.frame]
                
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
                
        if self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0

        if self.rect.top < 0:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
                
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
