import pygame
import random


class Constant:
    def __init__(self, mode):
        # game upset
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.read())
        self.running = True
        pygame.display.set_icon(pygame.image.load('./resources/images/ending/restart-1.png'))  # 更改图标
        pygame.display.set_caption("chrome://dino")  # 标题
        self.screen_wide = 720
        self.screen_long = 1280
        self.velocity = 5
        self.frames = 120  # 帧率
        self.time = 0  # 计数器

        # ground
        self.ground_images = './resources/images/ground/ground.png'
        self.ground_long = 2400  # 图像长 2400
        self.ground_high = 520

        # cloud
        self.cloud_low = 400
        self.cloud_high = 100
        self.cloud_image = './resources/images/cloud/cloud.png'

        # dino
        self.sound_file = "./resources/audios/jump.mp3"
        self.dino_image_high = 520
        self.dino_image_left = 70
        self.dino_image_start = './resources/images/dinosaur/dinosaur-start.png'
        self.dino_image_run1 = './resources/images/dinosaur/dinosaur-run-1.png'
        self.dino_image_run2 = './resources/images/dinosaur/dinosaur-run-2.png'
        self.dino_image_jump = './resources/images/dinosaur/dinosaur-jump.png'
        self.dino_image_duck1 = './resources/images/dinosaur/dinosaur-duck-1.png'
        self.dino_image_duck2 = './resources/images/dinosaur/dinosaur-duck-2.png'
        self.dino_image_die = './resources/images/dinosaur/dinosaur-die-1.png'

        # cactus
        self.high_cactus = 520
        self.cactus_image = f'./resources{mode}/images/cactus/cactus-{random.randint(1, 6)}.png'

        # pterodactyl
        self.pterodactyl_high_range = (520, 460, 420)
        self.pterodactyl_image1 = f'./resources{mode}/images/pterodactyl/pterodactyl-1.png'
        self.pterodactyl_image2 = f'./resources{mode}/images/pterodactyl/pterodactyl-2.png'

        # Scoreboard
        self.score = 0
        self.images_num = []
        for i in range(11):
            self.images_num.append(f'./resources/images/scoreboard/scoreboard-{i}.png')
        self.images_num = tuple(self.images_num)
        self.image_hi = './resources/images/scoreboard/scoreboard-10.png'
        self.score_area = (20 * 5, 21)

        # EndingIcon
        self.icon_x = 1280 / 2
        self.game_over_y = 280
        self.restart_y = 360
        self.switch_T = 6
        self.game_over_image = f'./resources/images/ending/game-over.png'

        self.icon_image = []
        for i in range(1, 9):
            self.icon_image.append(f'./resources/images/ending/restart-{i}.png')
        # 结束按钮动画计数器
        self.icon_time = 0
        self.page_icon = 7

        # 两个用于反派生成的变量
        self.create_time = 0
        self.when_create = 100
