import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, constant):
        super().__init__()
        self.image = pygame.image.load(f'./resources/images/cactus/cactus-{random.randint(1, 6)}.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = constant.screen_long, constant.high_cactus
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, constant):
        if self.rect.right <= 0:
            self.kill()
        self.rect.left -= constant.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, constant):
        super().__init__()
        self.pterodactyl1 = pygame.image.load(constant.pterodactyl_image1)
        self.pterodactyl2 = pygame.image.load(constant.pterodactyl_image2)
        self.image = self.pterodactyl1
        self.high_pterodactyl = constant.pterodactyl_high_range[random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = constant.screen_long, self.high_pterodactyl
        self.mask = pygame.mask.from_surface(self.image)

    def switch(self, time):
        if time % 96 < 48:
            self.image = self.pterodactyl1
        else:
            self.image = self.pterodactyl2

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, constant):
        self.switch(constant.time)
        self.rect.left -= constant.velocity
        if self.rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
