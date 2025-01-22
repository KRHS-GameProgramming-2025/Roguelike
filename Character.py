import pygame

class baseCharacter():
    def __init__(self,
                 image, 
                 startPosition = [0, 0]):
        self.__init__(self, "placeholder.png", [0,0], startPos)
        self.imagesUp = [pygame.image.load("placeholder.png")]
        self.imagesUpRight = [pygame.image.load("placeholder.png")]
        self.imagesRight = [pygame.image.load("placeholder.png")]
        self.imagesDownRight = [pygame.image.load("placeholder.png")]
        self.imagesDown = [pygame.image.load("placeholder.png")]
        self.imagesDownLeft = [pygame.image.load("placeholder.png")]
        self.imagesLeft = [pygame.image.load("placeholder.png")]
        self.imagesUpLeft = [pygame.image.load("placeholder.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.maxSpeed = maxSpeed
        self.kind = "player"
        
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
                
        self.image = self.images[self.frame]
