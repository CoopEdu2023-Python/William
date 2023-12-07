import pygame
import scene
import dinosaur
import obstacle


def print_start():  # 显示开始提示
    font = pygame.font.Font(None, 75)  # 字体设置
    text = font.render('Press the space key to start the game', True, 'black')
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.bottom = 1280//2, 522
    screen.blit(text, text_rect)


# pygame setup
pygame.init()
screen_wide = 720
screen_high = 1280
screen = pygame.display.set_mode((screen_high, screen_wide))
clock = pygame.time.Clock()
running = True
pygame.key.set_repeat(30)  # enable continuous keyboard event
stage = ('start', 'run', 'jump', 'dead')

velocity = 5
D = dinosaur.Dinosaur()
G = scene.Ground()
C = obstacle.Cactus(1, 1)
P = obstacle.Pterodactyl()
frames = 120  # 帧率
time = 0  # 循环次数
cactus_stage = 0  # 仙人掌的运动阶段，0代表第一个开始运动，一次类推
pygame.display.set_caption("chrome://dino")  # 标题

# game start
while not pygame.key.get_pressed()[pygame.K_SPACE] and running:
    screen.fill("white")
    D.draw(screen)
    print_start()

    pygame.display.flip()
    clock.tick(frames)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# game loop
while running:
    time += 1
    velocity = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or
             event.type == pygame.KEYDOWN and event.key == pygame.K_UP) and
                (D.d_status == 'run' or D.d_status == 'duck')):
            if D.d_status == 'run':
                D.sound_jump = 1
            D.d_status = 'jump'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and D.d_status == 'run':
            D.d_status = 'duck'
        if not(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) and D.d_status == 'duck':
            D.d_status = 'run'

    # put objects  on screen
    for i in (G, D, C, P):
        i.draw(screen)
    # dino move
    D.update(time)
    P.update(time, velocity)
    # cactus move
    C.update(velocity)
    # move ground
    G.update(velocity)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(frames)


pygame.quit()
