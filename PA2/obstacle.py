import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, mode):
        super().__init__()
        self.screen_wide = 720
        self.screen_long = 1280
        self.high_cactus = 520
        self.cactus_image = f'./resources{mode}/images/cactus/cactus-{random.randint(1, 6)}.png'

        self.image = pygame.image.load(self.cactus_image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = self.screen_long, self.high_cactus
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, v):
        if self.rect.right <= 0:
            self.kill()
        self.rect.left -= v

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, mode):
        super().__init__()
        self.screen_wide = 720
        self.screen_long = 1280
        self.pterodactyl1 = pygame.image.load(f'./resources{mode}/images/pterodactyl/pterodactyl-1.png')
        self.pterodactyl2 = pygame.image.load(f'./resources{mode}/images/pterodactyl/pterodactyl-2.png')
        self.pterodactyl = self.pterodactyl1
        self.high_pterodactyl = (520, 460, 420)[random.randint(0, 2)]
        self.rect = self.pterodactyl.get_rect()
        self.rect.left, self.rect.bottom = 1280, self.high_pterodactyl
        self.mask = pygame.mask.from_surface(self.pterodactyl)

    def switch(self, time):
        if time % 96 < 48:
            self.pterodactyl = self.pterodactyl1
        else:
            self.pterodactyl = self.pterodactyl2

        self.mask = pygame.mask.from_surface(self.pterodactyl)

    def update(self, time, v):
        self.switch(time)
        self.rect.left -= v
        if self.rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.pterodactyl, self.rect)

