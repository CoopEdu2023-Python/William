import random
import pygame


class Cactus:
    def __init__(self):
        self.cactus1 = pygame.image.load(f'./resources/images/cactus/cactus-{random.randint(1, 6)}.png')
        self.rect_cactus = self.cactus1.get_rect()
        self.rect_x1 = random.randint(1280, 2560)
        self.rect_cactus.left, self.rect_cactus.bottom = self.rect_x1, 520

    def motion(self, v):
        self.rect_cactus.left -= v
        if self.rect_cactus.right <= 0:
            self.__init__()


class Pterodactyl:
    pass
