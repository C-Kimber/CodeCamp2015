import pygame
import CONSTANTCONFIG as CON
from Adventure import Adventure

def main():
    pygame.font.init()
    l = Adventure(CON.SCREEN_WIDTH, CON.SCREEN_HEIGHT, CON.FPS)
    l.main_loop()
    return

if __name__ == "__main__":
    main()