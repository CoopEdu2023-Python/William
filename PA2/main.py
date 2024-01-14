import random
import pygame
import scene
import dinosaur
import obstacle
import constant

# pygame setup
pygame.init()
# mode = input()
Constant = constant.Constant('')
clock = pygame.time.Clock()
pygame.key.set_repeat(30)  # enable continuous keyboard event
screen = pygame.display.set_mode((Constant.screen_long, Constant.screen_wide))
# 创建组
cactus_group = pygame.sprite.Group()
pterodactyl_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()
# 实例
Dinosaur = dinosaur.Dinosaur(Constant)
Ground = scene.Ground(Constant)
Scoreboard = scene.Scoreboard(Constant)
EndingIcon = scene.EndingIcon(Constant)


def print_start():  # 显示开始提示
    font = pygame.font.Font(None, 75)  # 字体设置
    text = font.render('Press the space key to start the game', True, 'black')
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.bottom = Constant.screen_long // 2, 522
    screen.blit(text, text_rect)


def kill_all(enemy_group):
    for enemy in enemy_group:
        enemy.kill()


# game start
while not pygame.key.get_pressed()[pygame.K_SPACE] and Constant.running:
    screen.fill("white")

    Dinosaur.draw(screen)
    print_start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    clock.tick(Constant.frames)

# game loop
while True:
    Constant.create_time += 1
    Constant.time += 1

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
        Constant.running = False

    # 最高分赋值
    Constant.high_score = Constant.score if Constant.score > Constant.high_score else Constant.high_score

    for i in (Ground, cloud_group, Dinosaur, cactus_group, pterodactyl_group, Scoreboard):
        i.update(Constant)

    # 创造敌人create enemy
    if Constant.create_time == Constant.when_create:
        if random.randint(0, 10):
            cactus_group.add(obstacle.Cactus(Constant))
        else:
            pterodactyl_group.add(obstacle.Pterodactyl(Constant))
        if len(cloud_group) < 3:
            cloud_group.add(scene.Cloud(Constant))
        Constant.when_create = random.randint(100, 300)
        Constant.create_time = 0

    # 死亡判定
    Dinosaur.whether_die(cactus_group)
    Dinosaur.whether_die(pterodactyl_group)

    # draw all
    for i in (Ground, Dinosaur, Scoreboard, cactus_group, pterodactyl_group):
        i.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    clock.tick(Constant.frames)

    while not Constant.running:
        with open('high_score.txt', 'w') as file:
            file.write(str(Constant.high_score))
        EndingIcon.update(Constant)
        if Constant.icon_time // Constant.switch_T < Constant.page_icon:
            Constant.icon_time += 1

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
                    Constant.__init__('')

                    kill_all(pterodactyl_group)
                    kill_all(cactus_group)

                    Dinosaur = dinosaur.Dinosaur(Constant)
                    Ground = scene.Ground(Constant)
                    Scoreboard = scene.Scoreboard(Constant)
                    EndingIcon = scene.EndingIcon(Constant)

        # flip() the display to put your work on screen
        pygame.display.flip()
        # limits FPS to 60
        clock.tick(Constant.frames)
