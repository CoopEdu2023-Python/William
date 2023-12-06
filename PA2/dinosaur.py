import pygame


class Dinosaur:
    def __init__(self):
        pygame.display.set_icon(pygame.image.load('./resources/images/ending/restart-1.png'))  # 更改图标

        self.d_start = pygame.image.load('./resources/images/dinosaur/dinosaur-start.png')
        self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')

        self.rect_start = self.d_start.get_rect()
        self.rect_run = self.d_run.get_rect()

        self.rect_start.left, self.rect_start.bottom = 70, 520
        self.rect_run.left, self.rect_run.bottom = 70, 520
        self.d_jump = 0
        self.v1 = 20

    def update(self, time):
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.d_jump:
            self.d_jump = 1
        if self.d_jump == 1:
            if self.v1 == 0:
                self.d_jump = 2
            else:
                self.rect_run.bottom -= self.v1/2
                self.v1 -= 0.5

        if self.d_jump == 2:
            if self.v1 == 20:
                self.d_jump = 0
            else:
                self.rect_run.bottom += self.v1 / 2
                self.v1 += 0.5

    def pose(self, time):
        if self.rect_run.bottom == 520:
            if time % 24 < 12:
                self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')
            else:
                self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-2.png')
        else:
            self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-jump.png')



