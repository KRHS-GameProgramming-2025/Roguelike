import pygame

class baseCharacter():
    def __init__(self,
                 image,
                 maxSpeed,
                 startPosition = [0, 0],
                 characterType = None):
        self.imagesUp = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesUpRight = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesRight = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesDownRight = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesDown = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesDownLeft = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesLeft = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.imagesUpLeft = [pygame.image.load("Sprite/Placeholders/placeholder.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.maxSpeed = maxSpeed
        if characterType != None:
            self.kind = characterType
        elif characterType == None:
            self.kind = "None"
        
        self.headingX = "none"
        self.headingY = "none"
        self.pointingX = "none"
        self.pointingY = "up"
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
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
                
        elif self.pointingX == "none" and self.pointingY == "up":
            self.images = self.imagesUp
        elif self.pointingX == "right" and self.pointingY == "up":
            self.images = self.imagesUpRight
        elif self.pointingX == "right" and self.pointingY == "none":
            self.images = self.imagesRight
        elif self.pointingX == "right" and self.pointingY == "down":
            self.images = self.imagesDownRight
        elif self.pointingX == "none" and self.pointingY == "down":
            self.images = self.imagesDown
        elif self.pointingX == "left" and self.pointingY == "down":
            self.images = self.imagesDownLeft
        elif self.pointingX == "left" and self.pointingY == "none":
            self.images = self.imagesLeft
        elif self.pointingX == "left" and self.pointingY == "up":
            self.images = self.imagesUpLeft
            
        self.image = self.images[self.frame]
