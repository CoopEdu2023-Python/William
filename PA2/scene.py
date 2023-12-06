import pygame


class Ground:
    def __init__(self):
        self.ground1 = pygame.image.load('./resources/images/ground/ground.png')
        self.ground2 = pygame.image.load('./resources/images/ground/ground.png')
        self.rect1 = self.ground1.get_rect()
        self.rect2 = self.ground2.get_rect()
        self.rect1.left, self.rect1.bottom = 0, 520
        self.rect2.left, self.rect2.bottom = 2400, 520

    def update(self, v):
        self.rect1.left -= v
        if self.rect1.right <= 0:
            self.rect1.left = 2400

        self.rect2.left -= v
        if self.rect2.right <= 0:
            self.rect2.left = 2400


class Cloud:
    pass


class Scoreboard:
    pass


class Moon:
    pass


class Star:
    pass


class Endinglcon:
    pass

