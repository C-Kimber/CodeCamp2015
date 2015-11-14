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
        self.fieldwidth = width - 200
        self.upper_limit = self.width/2
        self.time = 10
        self.time2 = 1
        self.blonde = Blondie(40,80, self.width/2,self.height/2,(155,155,0))

        # surface = pygame.image.load('soda cans.png').convert()
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.mx,self.my = mouse_position
        if 1 in buttons:
            self.buttonon = True
        else:
            self.buttonon = False
            self.onrect = False

        clock = pygame.time.Clock()
        self.milliseconds = clock.tick(dynamicConfig.fps)  # milliseconds passed since last frame
        self.seconds = self.milliseconds / 1000.0

        self.time -= self.seconds
        self.time2 -= self.seconds*2

        if self.time2 <= 0:
            self.blonde.x = random.randint(50,630)

            self.blonde.y = random.randint (20, 200)
            self.time2 = 1

        if self.time <= 0:
            dynamicConfig.whatGame = dynamicConfig.randGame()
            dynamicConfig.health -= 1
            pygame.mouse.set_visible(True)
            CON.runGame()

        if self.blonde.health <=0:
            dynamicConfig.whatGame = dynamicConfig.randGame()
            dynamicConfig.score += 50
            pygame.mouse.set_visible(True)
            dynamicConfig.completedGames += 1
            CON.runGame()
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
        pygame.mouse.set_visible(False)
        self.background = pygame.image.load('blonde/tree.png').convert()
        blonde = pygame.image.load('blonde/mrjack.png').convert()
        blonde.set_colorkey((255,255,255))

        surface.blit(self.background, (0,0))
        surface.blit(blonde,(self.blonde.x-80,self.blonde.y-60))
        #self.blonde.draw(surface)
        mx, my = pygame.mouse.get_pos()



        rect = pygame.Rect(self.blonde.x,self.blonde.y,self.blonde.width,self.blonde.height)
        x,y,w,h = rect
        #if self.hover(x,y,w,h)==True:

         #   surface.fill((155,0,0),rect )
        #else:
         #   surface.fill((255,0,0),rect )
        if self.button(x, y, w, h):
            self.blonde.health -= 1


        rect = pygame.Rect(mx-20,my,10,5)
        surface.fill((155,0,0),rect )
        rect = pygame.Rect(mx+15,my,10,5)
        surface.fill((155,0,0),rect )
        rect = pygame.Rect(mx,my-20,5,10)
        surface.fill((155,0,0),rect )
        rect = pygame.Rect(mx,my+15,5,10)
        surface.fill((155,0,0),rect )



        label = self.font2.render("Time: "+str("%.2f" % round(self.time,2)), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 100))
        label = self.font2.render("Blondie: "+str(self.blonde.health), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 60))
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
