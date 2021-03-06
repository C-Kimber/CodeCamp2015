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
        (mouse_x,mouse_y) = mouse_position
        clock = pygame.time.Clock()
        milliseconds = clock.tick(dynamicConfig.fps)
        seconds = milliseconds / 1000.0
        if 1 in newbuttons:
            self.buttonon = True
        else:
            self.buttonon = False

        return



    def draw(self,surface):
        background  = pygame.image.load('starsbackground.png').convert()
        surface.blit(background, (0,0))
        myfont = self.font
        lable = myfont.render("Code Camp Stories", 1, (255,255,0))
        surface.blit(lable,(370,155))
        button = pygame.image.load('Pressedplaybutton.png').convert()
        button2 = pygame.image.load('Playbutton.png').convert()

        rect = pygame.Rect(450,350,100,50)
        surface.fill((255,255,255),rect)
        mx, my = pygame.mouse.get_pos()
        x,y,w,h = rect
        if self.hover(mx,my,x,y,w,h):
            surface.blit(button, (x,y))
        else:
         surface.blit(button2, (x,y))

        if self.button(mx,my,x,y,w,h) == True:
            dynamicConfig.whatGame = dynamicConfig.randGame()
            CON.runGame()

        return

    def button(self,mx,my, x, y, w, h):
        if x <= mx <= x + w and y <= my <= y + h:
            if self.buttonon == True:
                return True

    def hover(self,mx,my, x, y, w, h):
        if x <= mx <= x + w and y <= my <= y + h:
            return True

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
