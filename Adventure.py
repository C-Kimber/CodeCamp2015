import pygame
import dynamicConfig
from game_mouse import Game
from Data import Data
from menuData import Data as menuData
from RaindanceData import RaindanceData
from DeathData import DeadData
from chugData import Data as chugData

from Blondness_in_the_trees import Data as blondData


class Adventure(Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.bigData.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        if dynamicConfig.paused == False:
            self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        self.bigData.draw(surface)
        self.data.draw(surface)
        if dynamicConfig.paused == True:
            self.bigData.drawPaused(surface)

        return



    def newGame(self,width, height, frame_rate):
        global data
        name = 'CodeCamp2015'
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        if dynamicConfig.whatGame == 0:
            data = menuData(width, height, frame_rate)
        elif dynamicConfig.whatGame == 1:
            data = RaindanceData(width, height, frame_rate)
        elif dynamicConfig.whatGame == 2:
            data = blondData(width,height,frame_rate)
        elif dynamicConfig.whatGame == 3:
            data = chugData(width, height, frame_rate)

        elif dynamicConfig.whatGame == 99:
            data = DeadData(width,height,frame_rate)
        Game.__init__(self, name, width, height, frame_rate)
        self.data = data
        self.bigData = Data(width,height, frame_rate)
        return

