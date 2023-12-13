import pygame


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, constant):
        super().__init__()
        self.dino = pygame.image.load(constant.dino_image_start)
        self.sound = pygame.mixer.Sound(constant.sound_file)
        self.rect = self.dino.get_rect()
        self.rect.left, self.rect.bottom = constant.dino_image_left, constant.dino_image_high
        self.v1, self.d_status, self.sound_jump = 20, 'run', 0
        self.v0 = self.v1
        self.mask = pygame.mask.from_surface(self.dino)  # create mask for collision detection

    def switch_pose(self, constant):
        if self.d_status == 'die':
            self.dino = pygame.image.load(constant.dino_image_die)
        elif self.rect.bottom == constant.dino_image_high:
            if constant.time % 24 < 12:
                if self.d_status == 'run' or self.d_status == 'fall':
                    self.dino = pygame.image.load(constant.dino_image_run1)
                else:
                    self.dino = pygame.image.load(constant.dino_image_duck1)
            else:
                if self.d_status == 'run' or self.d_status == 'fall':
                    self.dino = pygame.image.load(constant.dino_image_run2)
                else:
                    self.dino = pygame.image.load(constant.dino_image_duck2)
        else:
            self.dino = pygame.image.load(constant.dino_image_jump)
        self.mask = pygame.mask.from_surface(self.dino)  # create mask for collision detection

    def whether_die(self, enemy_group):
        for enemy in enemy_group:
            if pygame.sprite.collide_mask(self, enemy):
                self.d_status = 'die'

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
