import pygame


class Dinosaur:
    def __init__(self):
        pygame.display.set_icon(pygame.image.load('./resources/images/Chrome.png'))
        self.d_start = pygame.image.load('./resources/images/dinosaur/dinosaur-start.png')
        self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')
        self.d_jump = pygame.image.load('./resources/images/dinosaur/dinosaur-jump.png')

        self.rect_start = self.d_start.get_rect()
        self.rect_run = self.d_run.get_rect()
        self.rect_jump = self.d_jump.get_rect()

        self.rect_start.left, self.rect_start.bottom = 70, 522
        self.rect_run.left, self.rect_run.bottom = 70, 522
        self.rect_jump.left, self.rect_jump.bottom = 70, 522

    def run(self, time):
        if time % 12 < 6:
            self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')
        else:
            self.d_run = pygame.image.load('./resources/images/dinosaur/dinosaur-run-2.png')

