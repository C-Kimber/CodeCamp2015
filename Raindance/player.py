import pygame
import dynamicConfig as dCON


class Player():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 3
        self.vel = 0
        return

    def moveLeft(self):
        self.vel -= 2
        return

    def moveRight(self):
        self.vel += 2

        return

    def moveUp(self):
        self.y -= 0
        return

    def moveDown(self):
        self.y += 0
        return

    def tick(self,board_height, upper_limit):
        self.x += self.vel

        if self.vel > 0:
            self.vel -= 1
        elif self.vel < 0:
            self.vel += 1

        if self.x < 0:
            self.x = 0
            self.vel = 0
        if self.x > upper_limit-self.width:
            self.x = upper_limit-self.width
            self.vel = 0
        if self.y < 0:
            self.y = 0
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def getDimensions(self):
        return self.x, self.y, self.width, self.height

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return


