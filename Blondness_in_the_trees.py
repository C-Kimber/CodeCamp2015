__author__ = 'Rob'
import pygame
import dynamicConfig
import CONSTANTCONFIG as CON
from blonde.blondie import Blondie
import random



RED = (255,0,0)
DRED = (102,0,0)
BRED = (255,51,51)
ORANGE = (255,128,0)
DORANGE = (204,102,0)
YELLOW = (255,255,0)




class Data:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/2
        self. time = 1
        self.blonde = Blondie(20,20, self.width/2,self.height/2,(155,155,0))
        try:
            self.background = surface = pygame.image.load('blonde/tree.png').convert()
        except:
            print "can't import tree"
        # surface = pygame.image.load('soda cans.png').convert()
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        (mouse_x,mouse_y) = mouse_position
        clock = pygame.time.Clock()
        milliseconds = clock.tick(CON.FPS)
        seconds = milliseconds / 1000.0
        self.time -= seconds
        if self.time <= 0:
            self.blonde.x = random.randint(50,400)

            self.blonde.y = random.randint (20, 200)
            self.time = 1


        return



    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,191,255),rect )
        surface.blit(self.background, (0,0))
        self.blonde.draw(surface)
        return

    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
