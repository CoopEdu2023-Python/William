import pygame
import random


class Ground:
    def __init__(self, constant):
        self.ground1 = pygame.image.load(constant.ground_images)
        self.ground2 = pygame.image.load(constant.ground_images)
        self.rect1 = self.ground1.get_rect()
        self.rect2 = self.ground2.get_rect()
        self.rect1.left, self.rect1.bottom = 0, constant.ground_high
        self.rect2.left, self.rect2.bottom = constant.ground_long, constant.ground_high

    def update(self, constant):
        self.rect1.left -= constant.velocity
        if self.rect1.right <= 0:
            self.rect1.left = constant.ground_long

        self.rect2.left -= constant.velocity
        if self.rect2.right <= 0:
            self.rect2.left = constant.ground_long

    def draw(self, screen):
        screen.blit(self.ground1, self.rect1)
        screen.blit(self.ground2, self.rect2)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, constant):
        super().__init__()
        self.cloud_image = pygame.image.load(constant.cloud_image)
        self.rect = self.cloud_image.get_rect()
        self.rect.left, self.rect.bottom = constant.screen_long, random.randint(constant.cloud_high, constant.cloud_low)

    def update(self, constant):
        self.rect.left -= constant.velocity * 0.5
        if self.rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.cloud_image, self.rect)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, constant):
        super().__init__()
        # images元组创建
        self.images = list()
        for i in range(11):
            self.images.append(pygame.image.load(constant.images_num[i]))
        self.images = tuple(self.images)

        self.image_score, self.image_hi_score = pygame.Surface(constant.score_area), pygame.Surface(constant.score_area)

        self.image_hi = pygame.image.load(constant.image_hi)

    def update(self, constant):
        constant.score = int(constant.time * constant.velocity * 0.015)
        self.image_score.fill('white')
        self.image_hi_score.fill('white')
        __score_list, __high_score_list = list(str(int(constant.score))), list(str(constant.high_score))

        for i in range(5 - len(__score_list)):
            __score_list.insert(0, '0')
        for i in range(5 - len(__high_score_list)):
            __high_score_list.insert(0, '0')

        for i in range(5):
            self.image_score.blit(self.images[int(__score_list[i])], (20 * i, 0))
            self.image_hi_score.blit(self.images[int(__high_score_list[i])], (20 * i, 0))

    def draw(self, screen):
        score_y, score_x, hi_score_x, hi_rect_x = 40, 1140, 1010, 960
        screen.blit(self.image_hi, (hi_rect_x, score_y))
        screen.blit(self.image_score, (score_x, score_y))
        screen.blit(self.image_hi_score, (hi_score_x, score_y))


class Moon:
    pass


class Star:
    pass


class EndingIcon:
    def __init__(self, constant):

        self.game_over = pygame.image.load(constant.game_over_image)
        self.rect_game_over = self.game_over.get_rect()
        self.rect_game_over.center = (constant.icon_x, constant.game_over_y)
        self.restart = pygame.image.load(constant.icon_image[1])
        self.rect_restart = self.restart.get_rect()
        self.rect_restart.center = (constant.icon_x, constant.restart_y)

    def update(self, constant):
        self.restart = pygame.image.load(constant.icon_image[constant.icon_time // constant.switch_T])

    def draw(self, screen):
        screen.blit(self.game_over, self.rect_game_over)
        screen.blit(self.restart, self.rect_restart)
