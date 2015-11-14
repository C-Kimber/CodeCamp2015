__author__ = 'Kimbe'
import pygame
import dynamicConfig
import CONSTANTCONFIG as CON
import random


class DeadData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/2
        self.wx = 0
        self.wy = 0
        self.buttonon = False

        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mx,self.my = mouse_position
        if 1 in newbuttons:
            self.buttonon = True
        else:
            self.buttonon = False
        return

    def button(self, x, y, w, h):
        mx, my = pygame.mouse.get_pos()
        if x <= mx <= x + w and y <= my <= y + h:
            if self.buttonon == True:
                return True

    def hover(self, x, y, w, h):
        mx, my = pygame.mouse.get_pos()
        if x <= mx <= x + w and y <= my <= y + h:
            return True



    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((55,55,55),rect )
        label = self.font.render("Games Completed: "+str(dynamicConfig.completedGames), 1, (255, 255, 0))
        surface.blit(label, (self.width/2-200,self.height/3))
        label = self.font.render("Score: "+str(dynamicConfig.score), 1, (255, 255, 0))
        surface.blit(label, (self.width/2-100,self.height/2))

        rect= pygame.Rect(self.width/2-50,self.height/2+100,80,60)
        x,y,w,h = rect
        if self.hover(x,y,w,h)==True:
            surface.fill((100,100,100),rect )
        else:
            surface.fill((155,155,155),rect )
        if self.button(x, y, w, h):
            dynamicConfig.whatGame = 0
            CON.reset()
            CON.runGame()


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

