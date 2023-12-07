import pygame


class Dinosaur:
    def __init__(self):
        self.sound_file = "./resources/audios/jump.mp3"
        self.dino_image_high = 520
        self.dino_image_left = 70
        self.dino_image_start = './resources/images/dinosaur/dinosaur-start.png'
        self.dino_image_run1 = './resources/images/dinosaur/dinosaur-run-1.png'
        self.dino_image_run2 = './resources/images/dinosaur/dinosaur-run-2.png'
        self.dino_image_jump = './resources/images/dinosaur/dinosaur-jump.png'
        self.dino_image_duck1 = './resources/images/dinosaur/dinosaur-duck-1.png'
        self.dino_image_duck2 = './resources/images/dinosaur/dinosaur-duck-2.png'
        self.dino = pygame.image.load(self.dino_image_start)
        self.sound = pygame.mixer.Sound(self.sound_file)
        self.rect_dino = self.dino.get_rect()
        self.rect_dino.left, self.rect_dino.bottom = self.dino_image_left, self.dino_image_high

        self.v1, self.d_status, self.sound_jump = 20, 'run', 0
        self.v0 = self.v1

    def update(self, time):
        if self.sound_jump:
            self.sound.play()
            self.sound_jump = 0

        if self.d_status == 'jump':
            if self.v1 == 0:
                self.d_status = 'fall'
            else:
                self.rect_dino.bottom -= self.v1 / 2
                self.v1 -= 0.5

        if self.d_status == 'fall':
            if self.v1 == self.v0:
                self.d_status = 'run'
            else:
                self.rect_dino.bottom += self.v1 / 2
                self.v1 += 0.5

        print(self.d_status, self.v0, self.v1)
        if self.rect_dino.bottom == self.dino_image_high:
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

    def draw(self, screen):
        screen.blit(self.dino, self.rect_dino)
