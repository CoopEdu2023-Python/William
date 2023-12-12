import random
import pygame
import scene
import dinosaur
import obstacle
import constant


Constant_num = constant.Constant()


def print_start():  # 显示开始提示
    font = pygame.font.Font(None, 75)  # 字体设置
    text = font.render('Press the space key to start the game', True, 'black')
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.bottom = Constant_num.screen_long // 2, 522
    screen.blit(text, text_rect)


# pygame setup
pygame.init()

high_score = 0
# 结束按钮动画计数器
icon_time = 0
page_icon = 7
# 两个用于反派生成的变量
create_time = 0
when_create = 100
mode = input()

clock = pygame.time.Clock()
running = True
pygame.key.set_repeat(30)  # enable continuous keyboard event

cactus_group = pygame.sprite.Group()
pterodactyl_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()


Dinosaur = dinosaur.Dinosaur(Constant_num)
Ground = scene.Ground(Constant_num)
Scoreboard = scene.Scoreboard()
EndingIcon = scene.EndingIcon()

screen = pygame.display.set_mode((Constant_num.screen_long, Constant_num.screen_wide))

# game start
while not pygame.key.get_pressed()[pygame.K_SPACE] and running:
    screen.fill("white")

    Dinosaur.draw(screen)
    print_start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    clock.tick(Constant_num.frames)

# game loop
while True:
    whether_create = 1
    cloud_num = 0
    create_time += 1
    Constant_num.time += 1
#    velocity += 0.1 if not time % 600 else 0
    # 初始化背景布
    screen.fill("white")
    # 键盘输入判断
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or
             event.type == pygame.KEYDOWN and event.key == pygame.K_UP) and
                (Dinosaur.d_status == 'run' or Dinosaur.d_status == 'duck')):
            if Dinosaur.d_status == 'run':
                Dinosaur.sound_jump = 1
            Dinosaur.d_status = 'jump'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and Dinosaur.d_status == 'run':
            Dinosaur.d_status = 'duck'
        if not(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) and Dinosaur.d_status == 'duck':
            Dinosaur.d_status = 'run'

    if Dinosaur.d_status == 'die':
        running = False

    # 最高分赋值
    high_score = Scoreboard.score if int(Scoreboard.score) > high_score else high_score
    print(high_score, Scoreboard.score)

    for i in (Ground, cloud_group, Dinosaur, cactus_group, pterodactyl_group):
        i.update(Constant_num)
    # print score
    Scoreboard.update(Constant_num.time, Constant_num.velocity, high_score)

    for cloud in cloud_group:
        cloud.draw(screen)
        cloud_num += 1

    # 创造敌人create enemy
    if create_time == when_create:
        if random.randint(0, 10):
            cactus_group.add(obstacle.Cactus(Constant_num, mode))
        else:
            pterodactyl_group.add(obstacle.Pterodactyl(Constant_num, mode))
        if cloud_num < 3 and whether_create % 2:
            cloud_group.add(scene.Cloud(Constant_num))
            whether_create += 0.5
        when_create = random.randint(100, 300)
        create_time = 0

    # 死亡判定
    for cactus in cactus_group:
        if pygame.sprite.collide_mask(Dinosaur, cactus):
            Dinosaur.d_status = 'die'

    for pterodactyl in pterodactyl_group:
        if pygame.sprite.collide_mask(Dinosaur, pterodactyl):
            Dinosaur.d_status = 'die'

    # draw all
    for i in (Ground, Dinosaur, Scoreboard, cactus_group, pterodactyl_group):
        i.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    clock.tick(Constant_num.frames)

    while not running:
        EndingIcon.update(icon_time)
        if icon_time // EndingIcon.switch_T < page_icon:
            icon_time += 1

        for i in (Ground, Scoreboard, EndingIcon, Dinosaur):
            i.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if ((EndingIcon.rect_restart.left < mouse_x < EndingIcon.rect_restart.left + EndingIcon.rect_restart.width) and
                        (EndingIcon.rect_restart.top < mouse_y < EndingIcon.rect_restart.top + EndingIcon.rect_restart.height)):
                    # upset
                    Constant_num.__init__()
                    # 结束按钮动画计数器
                    icon_time = 0
                    page_icon = 7
                    # 两个用于反派生成的变量
                    create_time = 0
                    when_create = 100

                    for pterodactyl in pterodactyl_group:
                        pterodactyl.kill()
                    for cactus in cactus_group:
                        cactus.kill()
                    Dinosaur = dinosaur.Dinosaur(Constant_num)
                    Ground = scene.Ground(Constant_num)
                    Scoreboard = scene.Scoreboard()
                    EndingIcon = scene.EndingIcon()

                    running = True

        # flip() the display to put your work on screen
        pygame.display.flip()
        # limits FPS to 60
        clock.tick(Constant_num.frames)
