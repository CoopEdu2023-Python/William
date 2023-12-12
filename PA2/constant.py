import pygame


class Constant:
    def __init__(self):
        pygame.display.set_caption("chrome://dino")  # 标题
        self.screen_wide = 720
        self.screen_long = 1280
        self.velocity = 5
        self.frames = 120  # 帧率
        self.time = 0  # 计数器

        # ground
        self.ground_long = 2400  # 图像长 2400
        self.ground_high = 520

        # cloud
        self.cloud_low = 400
        self.cloud_high = 100

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

        # pterodactyl
        self.pterodactyl_high_range = (520, 460, 420)