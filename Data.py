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
        self.buttonon = False





        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if 1 in newbuttons:
            self.buttonon = True
        else:
            self.buttonon = False

        if dynamicConfig.whatGame != 0:
            if pygame.K_ESCAPE in newkeys:
                dynamicConfig.paused = not dynamicConfig.paused


        if pygame.K_1 in newkeys:
            dynamicConfig.whatGame = 0
            CON.runGame()

        if pygame.K_2 in newkeys:
            dynamicConfig.whatGame = 1
            CON.runGame()

        if pygame.K_3 in newkeys:
            dynamicConfig.whatGame = 2
            CON.runGame()

        if pygame.K_4 in newkeys:
            dynamicConfig.whatGame = 3
            CON.runGame()

        if dynamicConfig.health <= 0:
            dynamicConfig.whatGame = 99
            dynamicConfig.health = .1
            CON.runGame()


        clock = pygame.time.Clock()
        milliseconds = clock.tick(dynamicConfig.fps)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0

        dynamicConfig.fps = CON.FPS + dynamicConfig.completedGames

        return



    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((55,55,55),rect )
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

    def drawPaused(self,surface):
        pygame.mouse.set_visible(True)
        rect = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, 200))
        surface.blit(rect, (0,0))

        rect = pygame.Surface((self.width/3,self.height/3+200), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, 200))
        surface.blit(rect, (self.width/2-200,150))
        label = self.font.render(("Paused"), 1, (255, 255, 0))
        surface.blit(label, (self.width/2-100,self.height/3))

        rect = pygame.Surface((120,60), pygame.SRCALPHA, 32)



        if self.hover(self.width/2-105,300,100,50):
            rect.fill((55, 55, 55, 200))
        else:
            rect.fill((255, 255, 255, 200))
        if self.button(self.width/2-105,300,100,50):
            rect.fill((0, 0, 0, 200))
            CON.reset()
            dynamicConfig.whatGame = 0
            dynamicConfig.paused = False
            CON.runGame()


        surface.blit(rect, (self.width/2-105,300))

        label = self.font.render(("Restart"), 1, (0, 0, 0))
        surface.blit(label, (self.width/2-100,self.height/2))

        rect = pygame.Surface((120,50), pygame.SRCALPHA, 32)
        if self.hover(self.width/2-105,400,100,50):
            rect.fill((55, 55, 55, 200))
        else:
            rect.fill((255, 255, 255, 200))
        if self.button(self.width/2-105,400,100,50):
            rect.fill((0, 0, 0, 200))
            dynamicConfig.paused = False

        surface.blit(rect, (self.width/2-105,400))

        label = self.font.render(("Resume"), 1, (0, 0, 0))
        surface.blit(label, (self.width/2-100,self.height/2+100))
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
