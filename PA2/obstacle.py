import random
import pygame


class Cactus:
    def __init__(self, c1, c2):
        self.screen_wide = 720
        self.screen_long = 1280
        self.high_cactus = 520
        self.cactus_image = f'./resources/images/cactus/cactus-{random.randint(1, 6)}.png'
        if c1:
            self.cactus1 = pygame.image.load(self.cactus_image)
            self.rect_cactus1 = self.cactus1.get_rect()
            self.rect_ran = random.randint(self.screen_long, int(self.screen_long * 1.3))
            self.rect_cactus1.left, self.rect_cactus1.bottom = self.rect_ran, self.high_cactus
        if c2:
            self.cactus2 = pygame.image.load(self.cactus_image)
            self.rect_cactus2 = self.cactus2.get_rect()
            self.rect_ran = random.randint(self.screen_long, int(self.screen_long * 1.3)) + self.rect_ran
            self.rect_cactus2.left, self.rect_cactus2.bottom = self.rect_ran, self.high_cactus

    def update(self, v):
        if self.rect_cactus1.right <= 0 or -200 < self.rect_cactus1.left - self.rect_cactus2.left < 200:
            self.__init__(1, 0)
        if self.rect_cactus2.right <= 0 or -200 < self.rect_cactus2.left - self.rect_cactus1.left < 200:
            self.__init__(0, 1)

        self.rect_cactus1.left -= v
        self.rect_cactus2.left -= v

    def draw(self, screen):
        screen.blit(self.cactus1, self.rect_cactus1)
        screen.blit(self.cactus2, self.rect_cactus2)


class Pterodactyl:
    def __init__(self):
        self.screen_wide = 720
        self.screen_long = 1280
        self.pterodactyl1 = './resources/images/pterodactyl/pterodactyl-1.png'
        self.pterodactyl2 = './resources/images/pterodactyl/pterodactyl-2.png'
        self.pterodactyl = pygame.image.load(self.pterodactyl1)
        self.high_pterodactyl = (520, 460, 420)[random.randint(0, 2)]
        self.rect_pterodactyl = self.pterodactyl.get_rect()
        self.rect_pterodactyl.left, self.rect_pterodactyl.bottom = 1280, self.high_pterodactyl

    def draw(self, screen):
        screen.blit(self.pterodactyl, self.rect_pterodactyl)

    def update(self, time, v):
        if time % 96 < 48:
            self.pterodactyl = pygame.image.load(self.pterodactyl1)
        else:
            self.pterodactyl = pygame.image.load(self.pterodactyl2)

        self.rect_pterodactyl.left -= v / 1.1
        if self.rect_pterodactyl.right <= 0:
            self.__init__()
