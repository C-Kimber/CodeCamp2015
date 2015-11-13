import pygame
from game_mouse import Game
from Data import Data

class Adventure(Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        self.data.draw(surface)
        return


    def newGame(self,width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        Game.__init__(self, "CodeCamp2015", width, height, frame_rate)
        self.data = Data(width,height,frame_rate)

        return
