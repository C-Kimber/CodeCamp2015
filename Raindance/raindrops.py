import pygame

class Drop():

    def __init__(self,width, height,x,y,color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.alive = True
        self.bounces = 0
        self.hit = False
        return
    #pygame.draw.circle(surface, (0,0,255), (50,50), 50, 2) # blue circle

    def hitObject(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.hit = True


    def setAlive(self,alive):
        self.alive = alive

    def tick(self,bottom):
        self.vel += 1
        if self.y-self.height >= bottom:
            self.vel = 0
            self.vel -= -3
            self.bounces += 1
            self.width -= 2
            self.height -= 2
        if self.bounces >=3:
            self.alive = False

        self.y += self.vel

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def draw(self,surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
