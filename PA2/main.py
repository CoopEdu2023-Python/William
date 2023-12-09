import random
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
screen_long = 1280
velocity = 5
frames = 120  # 帧率
time = 0  # 计数器
# 结束按钮动画计数器
icon_time = 0
page_icon = 7
# 两个用于反派生成的变量
create_time = 0
when_create = 100

screen = pygame.display.set_mode((screen_long, screen_wide))
clock = pygame.time.Clock()
running = True
pygame.key.set_repeat(30)  # enable continuous keyboard event

cactus_group = pygame.sprite.Group()
pterodactyl_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()

D = dinosaur.Dinosaur()
G = scene.Ground()
S = scene.Scoreboard()
E = scene.EndingIcon()

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
while True:
    whether_create = 1
    cloud_num = 0
    create_time += 1
    time += 1
    velocity = 5
    # 初始化背景布
    screen.fill("white")
    # 键盘输入判断
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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

    if D.d_status == 'die':
        running = False

    cactus_group.update(velocity)
    pterodactyl_group.update(time, velocity)
    cloud_group.update(velocity)
    # dino move
    D.update(time)
    # move ground
    G.update(velocity)
    # print score
    S.update(time, velocity)
    # put objects  on screen

    for cactus in cactus_group:
        cactus.draw(screen)
        if pygame.sprite.collide_mask(D, cactus):
            D.d_status = 'die'

    for pterodactyl in pterodactyl_group:
        pterodactyl.draw(screen)
        if pygame.sprite.collide_mask(D, pterodactyl):
            D.d_status = 'die'

    for cloud in cloud_group:
        cloud.draw(screen)
        cloud_num += 1

    # 创造敌人create enemy
    if create_time == when_create:
        if random.randint(0, 10):
            cactus_group.add(obstacle.Cactus())
        else:
            pterodactyl_group.add(obstacle.Pterodactyl())
        if cloud_num < 3 and whether_create % 2:
            cloud_group.add(scene.Cloud())
            whether_create += 0.5
        when_create = random.randint(50, 250)
        create_time = 0

    # draw 地面和恐龙

    for i in (G, D, S):
        i.draw(screen)

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (E.rect_restart.left < mouse_x < E.rect_restart.left + E.rect_restart.width) and (E.rect_restart.top < mouse_y < E.rect_restart.top + E.rect_restart.height):
                    # upset
                    # 结束按钮动画计数器
                    icon_time = 0
                    page_icon = 7
                    # 两个用于反派生成的变量
                    create_time = 0
                    when_create = 100
                    velocity = 5
                    time = 0  # 计数器
                    for pterodactyl in pterodactyl_group:
                        pterodactyl.kill()
                    for cactus in cactus_group:
                        cactus.kill()
                    D = dinosaur.Dinosaur()
                    G = scene.Ground()
                    S = scene.Scoreboard()
                    E = scene.EndingIcon()

                    running = True

        E.update(icon_time)
        if icon_time // E.switch_T < page_icon:
            icon_time += 1

        for i in (G, D, S, E):
            i.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()
        # limits FPS to 60
        clock.tick(frames)
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    clock.tick(frames)

