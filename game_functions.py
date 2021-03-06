import sys
import pygame
import random
from bullet import Bullet
from enemy import Enemy
from time import sleep

def check_events(xz_settings,screen,stats,sb,play_button,help_button,exit_button,plane,enemys,bullets,helpset,bullet_sound):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            # 用点击空格射击子弹
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_sound.play()
                    fire_bullet(xz_settings,screen,plane,bullets)
                elif event.key == pygame.K_q:
                    # print("q")
                    sys.exit()
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                # print(mouse_x,mouse_y)
                check_play_button(xz_settings,screen,stats,sb,play_button,help_button,exit_button,plane,enemys,bullets,helpset,mouse_x,mouse_y)

    # 让校长连续移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane.rect.left > 0:
        # print("LEFT")
        plane.rect.centerx -= xz_settings.plane_speed_factor
    if keys[pygame.K_RIGHT] and plane.rect.right < plane.screen_rect.right:
        # print("RIGHT")
        plane.rect.centerx += xz_settings.plane_speed_factor
    if keys[pygame.K_UP] and plane.rect.top > 0:
        # print("UP")
        plane.rect.centery -= xz_settings.plane_speed_factor
    if keys[pygame.K_DOWN] and plane.rect.bottom < plane.screen_rect.bottom:
        # print("DOWN")
        plane.rect.centery += xz_settings.plane_speed_factor

def check_play_button(xz_settings,screen,stats,sb,play_button,help_button,exit_button,plane,enemys,bullets,helpset,
mouse_x,mouse_y):
    """在点击Play时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏
        xz_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置状态，激活游戏
        stats.reset_stats()
        stats.game_active = True

        # 创建游戏时的背景音乐
        pygame.mixer.music.load("sounds/bgm4.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_level()
        sb.prep_plane()

        # 清空敌机列表和子弹列表
        enemys.empty()
        bullets.empty()

        # 让飞船居中
        plane.center_plane()
    elif help_button.rect.collidepoint(mouse_x,mouse_y):
        print("help")
        # 进入帮助页面
        stats.game_help = True

    elif helpset.back_button_rect.collidepoint(mouse_x,mouse_y):
        print("back")
        stats.game_help = False

    elif exit_button.rect.collidepoint(mouse_x,mouse_y):
        print("Exit")
        # 退出游戏
        sys.exit()
        pygame.quit()

        

def update_screen(xz_settings,stats,sb,screen,plane,enemys,bullets,helpset,play_button,help_button,exit_button):
    """ 更新屏幕上的图像，并且切换到屏幕"""

    # 绘制屏幕底色
    screen.fill(xz_settings.bg_color)
    
    # 如果游戏开始就绘制滚动背景
    if stats.game_active and not stats.game_help:
        xz_settings.reaction()
        screen.blit(xz_settings.bg_img,(0,xz_settings.bg_img_rect.y))
        screen.blit(xz_settings.bg_img2,(0,xz_settings.bg_img2_rect.y))
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        plane.blitme()
        enemys.draw(screen)

        # 显示计分器
        sb.show_score()

    # 如果游戏处于非激活状态，就绘制Play按钮，和Help按钮
    elif not stats.game_active and not stats.game_help:
        screen.blit(xz_settings.bg_img,(0,0))
        play_button.draw_button()
        help_button.draw_button()
        exit_button.draw_button()
 
    # 如果点击帮助界面就来到帮助界面
    elif stats.game_help:
        helpset.back_blitme()
        helpset.draw_help()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(xz_settings,screen,stats,sb,plane,enemys,bullets,enemy_down):
    """更新子弹的位置，删除消失的子弹"""

    # 更新子弹的位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
    # print(len(bullets))

    # 检查是否有子弹击中敌机，有就删除
    collisions = pygame.sprite.groupcollide(bullets,enemys,True,True)

    if collisions:
        for enemys in collisions.values():
            stats.score += xz_settings.enemy_points * len(enemys)
            sb.prep_score()
            enemy_down.play()
        if stats.score % xz_settings.level_scale == 0 and stats.score != 0:
            xz_settings.increase_speed()
            # 提高等级
            stats.level += 1
            sb.prep_level()

def fire_bullet(xz_settings,screen,plane,bullets):
    """射击子弹"""
    # print("SPACE")
    if len(bullets) < xz_settings.bullets_allowed:
        new_bullet = Bullet(xz_settings,screen,plane)
        bullets.add(new_bullet)

def create_fleet(xz_settings,screen,plane,enemys):
    """创建外星人群"""
    # 创建一个敌机
    if xz_settings.time == 0 and len(enemys) < xz_settings.enemys_sum:
        enemy0 = Enemy(xz_settings,(0,0),screen)
        enemy = Enemy(xz_settings,(random.randint(0,xz_settings.screen_width - enemy0.rect.width),0),screen)
        enemys.add(enemy)

def check_fleet_edges(xz_settings,enemys):
    """有敌机到达边缘就反向移动"""
    for enemy in enemys.sprites():
        if enemy.check_edges():
            enemy.direction *= -1
            break

def plane_hit(xz_settings,stats,sb,screen,plane,enemys,bullets):
    """响应敌机撞击飞船事件"""
    if stats.planes_left > 1:
        # 将planes_left -= 1
        stats.planes_left -= 1

        # 更新记分牌
        sb.prep_plane()

        # 清空敌机列表和子弹列表
        enemys.empty()
        bullets.empty()

        # 创建一群新的敌机，将飞船移动回初始位置
        # create_fleet(xz_settings,screen,plane,enemys)
        plane.center_plane()
        
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        # 加载背景音乐
        pygame.mixer.music.load("sounds/bgm3.ogg")
        pygame.mixer.music.play(loops=-1, start=0.0)

def check_enemy_botttom(xz_settings,stats,sb,screen,plane,enemys,bullets):
    """检查是否有敌机到达屏幕底端"""
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            # 像校长被撞一样的处理
            plane_hit(xz_settings,stats,sb,screen,plane,enemys,bullets)
            break

def update_enemys(xz_settings,stats,sb,screen,plane,enemys,bullets):
    """更新敌机的位置"""
    check_fleet_edges(xz_settings,enemys)
    enemys.update()
    create_fleet(xz_settings,screen,plane,enemys)
    # 检测敌机和飞船碰撞
    if pygame.sprite.spritecollideany(plane,enemys):
        # print("Plane hit!!!")
        plane_hit(xz_settings,stats,sb,screen,plane,enemys,bullets)
    
    # 检查是否有敌机越界
    check_enemy_botttom(xz_settings,stats,sb,screen,plane,enemys,bullets)
