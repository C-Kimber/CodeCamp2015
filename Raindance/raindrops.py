import pygame

class Drop(pygame.sprite.Sprite):






    def __init__(self,startpos,width, height,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = startpos
        return
    

    def draw(self,surface):
        pygame.draw.circle(surface, (0,0,255), (50,50), 50, 2) # red circle
