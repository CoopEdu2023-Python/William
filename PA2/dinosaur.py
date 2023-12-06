import pygame


class Dinosaur:
    def __init__(self):
        self.d_start = pygame.image.load('./resources/images/dinosaur/dinosaur-start.png')
        self.d_run1 = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')
        # self.d_run2 = pygame.image.load('./resources/images/dinosaur/dinosaur-run-2.png')
        self.d_jump = pygame.image.load('./resources/images/dinosaur/dinosaur-jump.png')

        self.rect_start = self.d_start.get_rect()
        self.rect_run1 = self.d_run1.get_rect()
        # self.rect_run2 = self.d_run2.get_rect()
        self.rect_jump = self.d_jump.get_rect()

        self.rect_start.left, self.rect_start.bottom = 52, 522
        self.rect_run1.left, self.rect_run1.bottom = 52, 522
        # self.rect_start.left, self.rect_start.bottom = 52, 522
        self.rect_jump.left, self.rect_jump.bottom = 52, 522

    def run(self, time):
        if time % 2:
            self.d_run1 = pygame.image.load('./resources/images/dinosaur/dinosaur-run-1.png')
        else:
            self.d_run1 = pygame.image.load('./resources/images/dinosaur/dinosaur-run-2.png')

