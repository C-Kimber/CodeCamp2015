import main

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 30


def runGame():
    main.main()

def button(self,mx,my, x, y, w, h):
        if x <= mx <= x + w and y <= my <= y + h:
            if self.buttonon == True:
                return True

def hover(self,mx,my, x, y, w, h):
    if x <= mx <= x + w and y <= my <= y + h:
        return True