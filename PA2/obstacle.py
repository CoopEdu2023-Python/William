import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, constant_num, mode):
        super().__init__()

        self.cactus_image = f'./resources{mode}/images/cactus/cactus-{random.randint(1, 6)}.png'
        self.image = pygame.image.load(self.cactus_image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = constant_num.screen_long, constant_num.high_cactus
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, constant_num):
        if self.rect.right <= 0:
            self.kill()
        self.rect.left -= constant_num.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, constant_num, mode):
        super().__init__()
        self.pterodactyl1 = pygame.image.load(f'./resources{mode}/images/pterodactyl/pterodactyl-1.png')
        self.pterodactyl2 = pygame.image.load(f'./resources{mode}/images/pterodactyl/pterodactyl-2.png')
        self.image = self.pterodactyl1
        self.high_pterodactyl = constant_num.pterodactyl_high_range[random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = constant_num.screen_long, self.high_pterodactyl
        self.mask = pygame.mask.from_surface(self.image)

    def switch(self, time):
        if time % 96 < 48:
            self.image = self.pterodactyl1
        else:
            self.image = self.pterodactyl2

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, constant_num):
        self.switch(constant_num.time)
        self.rect.left -= constant_num.velocity
        if self.rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
