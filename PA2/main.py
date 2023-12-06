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
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

stage = ('start', 'run', 'jump', 'dead')

velocity = 5
D = dinosaur.Dinosaur()
G = scene.Ground()
C1 = obstacle.Cactus()
C2 = obstacle.Cactus()
C3 = obstacle.Cactus()
frames = 120  # 帧率
time = 0  # 循环次数
cactus_stage = 0  # 仙人掌的运动阶段，0代表第一个开始运动，一次类推
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
    velocity = 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # put ground on screen
    screen.blit(G.ground1, G.rect1)
    screen.blit(G.ground2, G.rect2)
    screen.blit(D.d_run, D.rect_run)

    screen.blit(C1.cactus1, C1.rect_cactus)
    screen.blit(C2.cactus1, C2.rect_cactus)
    screen.blit(C3.cactus1, C3.rect_cactus)
    # dino move
    D.update(time)
    D.pose(time)
    # cactus move
    C1.motion(velocity)
    if C1.rect_cactus.left <= 640 and cactus_stage == 0:
        cactus_stage += 1
    if C2.rect_cactus.left <= 640 and cactus_stage == 1:
        cactus_stage += 1
    if cactus_stage:
        C2.motion(velocity)
    if cactus_stage == 2:
        C3.motion(velocity)
    # if -250 < C1.rect_cactus.centerx - C2.rect_cactus.centerx < 250:
    #     C2.change()
    # if -250 < C2.rect_cactus.centerx - C3.rect_cactus.centerx < 250:
    #     C3.change()
    # if -250 < C3.rect_cactus.centerx - C1.rect_cactus.centerx < 250:
    #     C1.change()

    # move ground
    G.update(velocity)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(frames)


pygame.quit()
