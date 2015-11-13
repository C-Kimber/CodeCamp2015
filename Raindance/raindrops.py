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
        return
    #pygame.draw.circle(surface, (0,0,255), (50,50), 50, 2) # blue circle

    def tick(self,bottom):
        self.vel += 1
        if self.y-self.height >= bottom:
            self.vel = 0
            self.vel -= -3
            self.bounces += 1
        if self.bounces >=3:
            self.alive = False

        self.y += self.vel

    def draw(self,surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
