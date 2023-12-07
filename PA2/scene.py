import pygame


class Ground:
    def __init__(self):
        pygame.display.set_icon(pygame.image.load('./resources/images/ending/restart-1.png'))  # 更改图标
        self.ground_long = 2400  # 图像长 2400
        self.ground_high = 520
        self.ground_images = './resources/images/ground/ground.png'
        self.ground1 = pygame.image.load(self.ground_images)
        self.ground2 = pygame.image.load(self.ground_images)
        self.rect1 = self.ground1.get_rect()
        self.rect2 = self.ground2.get_rect()
        self.rect1.left, self.rect1.bottom = 0, self.ground_high
        self.rect2.left, self.rect2.bottom = self.ground_long, self.ground_high

    def update(self, v):
        self.rect1.left -= v
        if self.rect1.right <= 0:
            self.rect1.left = self.ground_long

        self.rect2.left -= v
        if self.rect2.right <= 0:
            self.rect2.left = self.ground_long

    def draw(self, screen):
        screen.fill("white")
        screen.blit(self.ground1, self.rect1)
        screen.blit(self.ground2, self.rect2)


class Cloud:
    pass


class Scoreboard:
    pass


class Moon:
    pass


class Star:
    pass


class EndingIcon:
    pass

