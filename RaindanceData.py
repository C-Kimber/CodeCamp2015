__author__ = 'Kimbe'
import pygame
import dynamicConfig
from Raindance.raindrops import Drop
import CONSTANTCONFIG as CON
from Raindance.player import  Player
import random


RED = (255,0,0)
DRED = (102,0,0)
BRED = (255,51,51)
ORANGE = (255,128,0)
DORANGE = (204,102,0)
YELLOW = (255,255,0)




class RaindanceData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/2


        self.miliseconds = 0
        self.seconds =0

        self.player = Player(20,40,self.width/2,self.height-40,(255,255,255))


        self.drop_height = 20
        self.drop_width = 20
        self.drop_color = (0,0,255)

        self.drops = []


        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_a in keys:
            self.player.moveLeft()





        clock = pygame.time.Clock()
        self.milliseconds = clock.tick(CON.FPS)  # milliseconds passed since last frame
        self.seconds = self.milliseconds / 1000.0



        if self.milliseconds % 3 == 0:

            self.addDrop()

        for drop in self.drops:
            drop.tick(self.height-50)



        live_drops = []


        for drop in self.drops:
            if drop.alive:
                live_drops.append(drop)

        self.drops = live_drops


        return

    def addDrop(self):
        new_drop = Drop( self.drop_width, self.drop_height, random.randint(0,(self.width-self.drop_width)),random.randint(0,20), self.drop_color )
        self.drops.append( new_drop )

        return



    def draw(self,surface):
        self.player.draw(surface)
        for drop in self.drops:
            drop.draw(surface)
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
