import pygame
import scene
import dinosaur


def print_start():  # 显示开始提示
    font = pygame.font.Font(None, 75)  # 字体设置
    text = font.render('Press the space key to start the game', True, 'black')
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.bottom = 1280//2, 522
    screen.blit(text, text_rect)


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

pygame.display.set_caption("chrome://dino")  # 标题

# game start
while not pygame.key.get_pressed()[pygame.K_SPACE] and running:
    screen.fill("white")
    screen.blit(D.d_start, D.rect_start)
    print_start()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60

    clock.tick(frames)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    # dino move
    screen.blit(D.d_run, D.rect_run)

    D.update(time)
    D.pose(time)
    # move ground
    G.update(velocity)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(frames)

pygame.quit()
