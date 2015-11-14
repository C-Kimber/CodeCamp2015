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
        self.font_1 = pygame.font.SysFont("Times New Roman",18)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.fieldwidth = width - 200

        self.upper_limit = self.width/2



        self.miliseconds = 0
        self.seconds =0

        self.player = Player(20,40,self.width/2,self.height-40,(255,255,255))


        self.drop_height = 20
        self.drop_width = 20
        self.drop_color = (0,0,255)

        self.drops = []

        self.time = 10
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_a in keys:
            self.player.moveLeft()
        if pygame.K_d in keys:
            self.player.moveRight()
        if self.player.health <= 0:
            dynamicConfig.health -= 1
            dynamicConfig.whatGame = 0
            CON.runGame()



        clock = pygame.time.Clock()
        self.milliseconds = clock.tick(CON.FPS)  # milliseconds passed since last frame
        self.seconds = self.milliseconds / 1000.0



        self.player.tick(self.height, self.fieldwidth)

        if self.milliseconds % 3 == 0:

            self.addDrop()

        self.time -= self.seconds

        if self.time <= 0:
            dynamicConfig.whatGame = 0
            dynamicConfig.completedGames += 1
            dynamicConfig.score += 50* self.player.health
            CON.runGame()


        for drop in self.drops:
            drop.tick(self.height-50)

        for drop in self.drops:
            if not drop.alive:
                continue
            x,y,h,w = self.player.getDimensions()
            drop.hitObject(x,y,h,w)
            if drop.hit == True:
                drop.setAlive(False)
                self.player.health -= 1

        live_drops = []


        for drop in self.drops:
            if drop.alive:
                live_drops.append(drop)

        self.drops = live_drops


        return

    def addDrop(self):
        new_drop = Drop( self.drop_width, self.drop_height, random.randint(0,(self.fieldwidth-self.drop_width)),random.randint(0,20), self.drop_color )
        self.drops.append( new_drop )

        return



    def draw(self,surface):
        rect = pygame.Rect(0,0,self.fieldwidth,self.height)
        surface.fill((0,0,0),rect )
        myfont = self.font
        myfont2 = self.font2
        myfont3 = self.font_1
        label = myfont.render("Time"+str(self.time), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 20))
        label = myfont.render("lives: "+str(self.player.health), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 60))
        label = myfont3.render("chances left: "+str(dynamicConfig.health), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 100))
        label = myfont3.render("games completed: "+str(dynamicConfig.completedGames), 1, (255, 255, 0))
        surface.blit(label, (self.fieldwidth, 140))

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
