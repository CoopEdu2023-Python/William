import pygame


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.dino = pygame.image.load(self.dino_image_start)
        self.sound = pygame.mixer.Sound(self.sound_file)
        self.rect = self.dino.get_rect()
        self.rect.left, self.rect.bottom = self.dino_image_left, self.dino_image_high
        self.v1, self.d_status, self.sound_jump = 20, 'run', 0
        self.v0 = self.v1
        self.mask = pygame.mask.from_surface(self.dino)  # create mask for collision detection

    def switch_pose(self, time):
        if self.d_status == 'die':
            self.dino = pygame.image.load(self.dino_image_die)
        elif self.rect.bottom == self.dino_image_high:
            if time % 24 < 12:
                if self.d_status == 'run' or self.d_status == 'fall':
                    self.dino = pygame.image.load(self.dino_image_run1)
                else:
                    self.dino = pygame.image.load(self.dino_image_duck1)
            else:
                if self.d_status == 'run' or self.d_status == 'fall':
                    self.dino = pygame.image.load(self.dino_image_run2)
                else:
                    self.dino = pygame.image.load(self.dino_image_duck2)
        else:
            self.dino = pygame.image.load(self.dino_image_jump)
        self.mask = pygame.mask.from_surface(self.dino)  # create mask for collision detection

    def update(self, time):
        # jump模块
        if self.sound_jump:
            self.sound.play()
            self.sound_jump = 0

        if self.d_status == 'jump':
            if self.v1 == 0:
                self.d_status = 'fall'
            else:
                self.rect.bottom -= self.v1 / 2
                self.v1 -= 0.5

        if self.d_status == 'fall':
            if self.v1 == self.v0:
                self.d_status = 'run'
            else:
                self.rect.bottom += self.v1 / 2
                self.v1 += 0.5
        self.switch_pose(time)

    def draw(self, screen):
        screen.blit(self.dino, self.rect)
