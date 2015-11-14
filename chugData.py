__author__ = 'Kimbe'
import pygame
import dynamicConfig
import CONSTANTCONFIG as CON
import random


class Data:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.fieldwidth = width - 200
        self.upper_limit = self.width/2
        self.wx = 0
        self.wy = 0
        self.buttonon = False
        self.onrect = False
        self.rect= pygame.Rect(self.width/2+150,self.height/2+100,80,60)
        self.time = 25
        self.chugpoints = 0
        self.point_at = 500
        self.dcans = 0
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mx,self.my = mouse_position
        if 1 in buttons:
            self.buttonon = True
        else:
            self.buttonon = False
            self.onrect = False
        x,y,w,h = self.rect


        if y > 500:
            y = 500

        elif y < 100:
            y = 100
        self.wherePoint(y)
        self.rect = (x,y,w,h)

        if self.chugpoints >= 100:
            self.chugpoints = 0
            self.dcans += 1
        if self.dcans >= 3:
            dynamicConfig.score += 50
            dynamicConfig.whatGame = dynamicConfig.randGame()
            dynamicConfig.completedGames += 1
            dynamicConfig.score += 50*self.time
            CON.runGame()


        clock = pygame.time.Clock()
        self.milliseconds = clock.tick(dynamicConfig.fps)  # milliseconds passed since last frame
        self.seconds = self.milliseconds / 1000.0


        self.time -= self.seconds

        if self.time <= 0:
            dynamicConfig.whatGame = dynamicConfig.randGame()
            dynamicConfig.health -= 1
            CON.runGame()
        return

    def wherePoint(self, y):
        if self.point_at == 500:
            if y >= 499:
               self.point_at = 100
               self.chugpoints += 1
        if self.point_at == 100:
            if y <= 101:
                self.point_at = 500
                self.chugpoints += 1


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
        background = pygame.image.load('Chug/soda chug back ground.png').convert()
        mx, my = pygame.mouse.get_pos()
        surface.blit(background,(0,0))

        rect2= pygame.Rect(self.width/2+150,100,80,460)
        surface.fill((155,55,55),rect2 )


        x,y,w,h = self.rect
        if self.hover(x,y,w,h)==True:

            surface.fill((155,0,0),self.rect )
        else:
            surface.fill((255,0,0),self.rect )
        if self.button(x, y, w, h):
            self.onrect = True
        if self.onrect == True:
            self.rect = pygame.Rect(self.width/2+150,(my-30),80,60)



        label = self.font2.render("Chugged: "+str(self.chugpoints)+" %", 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 20))
        label = self.font2.render("Time : "+str("%.2f" % round(self.time,2)), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 60))
        label = self.font2.render("Downed: "+str(self.dcans), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 100))
        label = self.font2.render("Chances: "+str(dynamicConfig.health), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 140))
        label = self.font2.render("Completed: "+str(dynamicConfig.completedGames), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 180))



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
