import pygame
import random


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
        screen.blit(self.ground1, self.rect1)
        screen.blit(self.ground2, self.rect2)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cloud_low = 400
        self.cloud_high = 100
        self.screen_long = 1280
        self.cloud_image = './resources/images/cloud/cloud.png'
        self.cloud_image = pygame.image.load(self.cloud_image)
        self.rect = self.cloud_image.get_rect()
        self.rect.left, self.rect.bottom = self.screen_long, random.randint(self.cloud_high, self.cloud_low)

    def update(self, v):
        self.rect.left -= v*0.5
        if self.rect.right <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.cloud_image, self.rect)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score_y = 40
        self.score_x = 1140
        self.hi_score_x = 980
        self.score = 0
        self.score_list = []
        self.images = list()
        self.hi_image = '10'
        for i in range(11):
            self.images.append(pygame.image.load(f'./resources/images/scoreboard/scoreboard-{i}.png'))
        self.images = tuple(self.images)
        print(self.images)
        self.image_score = pygame.Surface((20 * 5, 21))
        self.image_hi_score = pygame.Surface((150, 21))

    def print_score(self, num: int):
        score_list = list(str(num))
        self.score = num

        for i in range(5 - len(score_list)):
            score_list.insert(0, '0')

        # add image to scoreboard
        for i in range(5):
            self.image_score.blit(self.images[int(score_list[i])], (20 * i, 0))

        self.image_score.set_alpha(255)  # use set_alpha to make surface background transparent

    def print_high_score(self, num: int):
        self.image_hi_score.fill((255, 255, 255))
        score_list = list(str(num))

        for i in range(5 - len(score_list)):
            score_list.insert(0, '0')
        score_list.insert(0, self.hi_image)

        # add image to scoreboard

        for i in range(6):
            __center_num = (0, 0) if i == 0 else (20 * (i+1) + 10, 0)
            self.image_hi_score.blit(self.images[int(score_list[i])], __center_num)

        self.image_hi_score.set_alpha(255)  # use set_alpha to make surface background transparent

    def update(self, time, v, high_score):
        self.score = time * v * 0.015
        self.image_score.fill('white')

        self.print_score(int(self.score))
        self.print_high_score(high_score)

    def draw(self, screen):
        screen.blit(self.image_score, (self.score_x, self.score_y))
        screen.blit(self.image_hi_score, (self.hi_score_x, self.score_y))


class Moon:
    pass


class Star:
    pass


class EndingIcon:
    def __init__(self):
        self.icon_x = 1280 / 2
        self.game_over_y = 280
        self.restart_y = 360
        self.switch_T = 6
        self.game_over_image = './resources/images/ending/game-over.png'
        self.game_over = pygame.image.load(self.game_over_image)
        self.rect_game_over = self.game_over.get_rect()
        self.rect_game_over.center = (self.icon_x, self.game_over_y)

        self.icon_image = []
        for i in range(1, 9):
            self.icon_image.append(f'./resources/images/ending/restart-{i}.png')

        self.restart = pygame.image.load(self.icon_image[1])
        self.rect_restart = self.restart.get_rect()
        self.rect_restart.center = (self.icon_x, self.restart_y)

    def update(self, icon_time):
        self.restart = pygame.image.load(self.icon_image[icon_time // self.switch_T])

    def draw(self, screen):
        screen.blit(self.game_over, self.rect_game_over)
        screen.blit(self.restart, self.rect_restart)
