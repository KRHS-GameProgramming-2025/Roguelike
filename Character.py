import pygame, math

class baseCharacter():
    def __init__(self,
                 image,
                 maxSpeed,
                 startPosition = [0, 0],
                 characterType = None):
        self.imagesUp = [pygame.image.load(image + "Up" + ".png")]
        self.imagesUpRight = [pygame.image.load(image + "UpRight" + ".png")]
        self.imagesRight = [pygame.image.load(image + "Right" + ".png")]
        self.imagesDownRight = [pygame.image.load(image + "DownRight" + ".png")]
        self.imagesDown = [pygame.image.load(image + "Down" + ".png")]
        self.imagesDownLeft = [pygame.image.load(image + "DownLeft" + ".png")]
        self.imagesLeft = [pygame.image.load(image + "Left" + ".png")]
        self.imagesUpLeft = [pygame.image.load(image + "UpLeft" + ".png")]
        self.imagesNone = [pygame.image.load(image + "Down" + ".png")]
        self.images = self.imagesNone
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
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
        self.pointingY = "none"

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
                
    def aim(self, mPos):
        m = mPos
        p = self.rect.center
        angle = math.degrees(math.atan2(m[1]-p[1], m[0]-p[0]))        
        
        if 0 < angle <= 22.5:
            self.images = self.imagesRight
        elif 22.5 < angle <= 67.5:
            self.images = self.imagesDownRight
        elif 67.5 < angle <= 112.5:
            self.images = self.imagesDown
        elif 112.5 < angle <= 157.5:
            self.images = self.imagesDownLeft
        elif 157.5 < angle <= 180:
            self.images = self.imagesLeft
        
        elif -180 < angle <= -157.5:
            self.images = self.imagesLeft
        elif -157.5 < angle <= -112.5:
            self.images = self.imagesUpLeft
        elif -112.5 < angle <= -67.5:
            self.images = self.imagesUp
        elif -67.5 < angle <= -22.5:
            self.images = self.imagesUpRight
        elif -22.5 < angle <= 0:
            self.images = self.imagesRight
            
        self.image = self.images[self.frame]
    
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
