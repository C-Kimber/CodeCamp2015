import pygame
import CONSTANTCONFIG as CON
import dynamicConfig
from Adventure import Adventure

def main():
    pygame.font.init()
    l = Adventure(CON.SCREEN_WIDTH, CON.SCREEN_HEIGHT, dynamicConfig.fps)
    l.main_loop()
    return

if __name__ == "__main__":
    main()