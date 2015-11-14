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
        (mouse_x,mouse_y) = mouse_position
        clock = pygame.time.Clock()
        milliseconds = clock.tick(CON.FPS)
        seconds = milliseconds / 1000.0

        return



    def draw(self,surface):
        background  = pygame.image.load('starsbackground.png').convert()
        surface.blit(background, (100,0))
        myfont = self.font
        lable = myfont.render("Code Camp Stories", 1, (255,255,0))
        surface.blit(lable,(100,100))
        button = pygame.image.load('Playbutton.png').convert()
        surface.blit(button, (200,200))
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
