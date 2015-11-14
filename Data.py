__author__ = 'Kimbe'
import pygame
import dynamicConfig
import CONSTANTCONFIG as CON
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

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_ESCAPE in newkeys:
            dynamicConfig.paused = not dynamicConfig.paused


        if pygame.K_1 in newkeys:
            dynamicConfig.whatGame = 0
            CON.runGame()

        if pygame.K_2 in newkeys:
            dynamicConfig.whatGame = 1
            CON.runGame()

        if dynamicConfig.health <= 0:
            dynamicConfig.whatGame = 99
            dynamicConfig.health = .1
            CON.runGame()


        clock = pygame.time.Clock()
        milliseconds = clock.tick(CON.FPS)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0



        return



    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((55,55,55),rect )
        return

    def drawPaused(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((255,255,255),rect )
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
