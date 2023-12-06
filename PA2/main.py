import pygame
import scene
import dinosaur


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

stage = ('start', 'run', 'jump', 'dead')

velocity = 10  # 速度（最好能整除2400）
D = dinosaur.Dinosaur()
G = scene.Ground()
frames = 60  # 帧率
time = 0  # 循环次数
# game loop

while running:
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # put ground on screen
    screen.blit(G.ground1, G.rect1)
    screen.blit(G.ground2, G.rect2)
    screen.blit(D.d_run1, D.rect_start)
    D.run(time)
    # move ground
    G.update(velocity)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(frames)

pygame.quit()