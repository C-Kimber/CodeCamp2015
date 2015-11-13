import pygame

from Adventure import Adventure

def main():
    pygame.font.init()
    l = Adventure(800, 600, 30)
    l.main_loop()
    return

if __name__ == "__main__":
    main()