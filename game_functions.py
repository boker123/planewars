import sys
import pygame
from bullet import Bullet
from enemy import Enemy
from time import sleep

def check_events(xz_settings,screen,stats,play_button,plane,enemys,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            # 用点击空格射击子弹
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_bullet(xz_settings,screen,plane,bullets)
                elif event.key == pygame.K_q:
                    print("q")
                    sys.exit()
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                print(mouse_x,mouse_y)
                check_play_button(xz_settings,screen,stats,play_button,plane,enemys,bullets,mouse_x,mouse_y)

    # 让校长连续移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane.rect.left > 0:
        print("LEFT")
        plane.rect.centerx -= xz_settings.plane_speed_factor
    if keys[pygame.K_RIGHT] and plane.rect.right < plane.screen_rect.right:
        print("RIGHT")
        plane.rect.centerx += xz_settings.plane_speed_factor
    if keys[pygame.K_UP] and plane.rect.top > 0:
        print("UP")
        plane.rect.centery -= xz_settings.plane_speed_factor
    if keys[pygame.K_DOWN] and plane.rect.bottom < plane.screen_rect.bottom:
        print("DOWN")
        plane.rect.centery += xz_settings.plane_speed_factor

def check_play_button(xz_settings,screen,stats,play_button,plane,enemys,bullets,
mouse_x,mouse_y):
    """在点击Play时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        if play_button.rect.collidepoint(mouse_x,mouse_y):
            stats.reset_stats()
            stats.game_active = True

            # 清空敌机列表和子弹列表
            enemys.empty()
            bullets.empty()

            # 创建一群敌机，让飞船居中
            create_fleet(xz_settings,screen,plane,enemys)
            plane.center_ship()

def update_screen(xz_settings,stats,screen,plane,enemys,bullets,play_button):
    """ 更新屏幕上的图像，并且切换到屏幕"""

    # 绘制屏幕
    screen.fill(xz_settings.bg_color)
    screen.blit(xz_settings.bg_img,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    enemys.draw(screen)

    # 如果游戏处于非激活状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(xz_settings,screen,plane,enemys,bullets):
    """更新子弹的位置，删除消失的子弹"""

    # 更新子弹的位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
    print(len(bullets))

    # 检查是否有子弹击中敌机，有就删除
    collisions = pygame.sprite.groupcollide(bullets,enemys,True,True)

    if len(enemys) == 0:
        bullets.empty()
        create_fleet(xz_settings,screen,plane,enemys)

def fire_bullet(xz_settings,screen,plane,bullets):
    """射击子弹"""
    # print("SPACE")
    if len(bullets) < xz_settings.bullets_allowed:
        new_bullet = Bullet(xz_settings,screen,plane)
        bullets.add(new_bullet)

def create_fleet(xz_settings,screen,plane,enemys):
    """创建外星人群"""

    # 创建一个敌机，计算可以容纳多少敌机
    enemy = Enemy(xz_settings,screen)
    enemy_width = enemy.rect.width
    available_space_x = xz_settings.screen_width - 2 * enemy_width
    number_enemys_x = int(available_space_x / (2 * enemy_width))

    # 创建一行敌机
    for enemy_number in range(number_enemys_x):
        # 创建一个敌机加入行
        enemy = Enemy(xz_settings,screen)
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemys.add(enemy)

def check_fleet_edges(xz_settings,enemys):
    """有敌机到达边缘就反向移动"""
    for enemy in enemys.sprites():
        if enemy.check_edges():
            change_fleet_direction(xz_settings,enemys)
            break

def change_fleet_direction(xz_settings,enemys):
    """将整群敌机向下移，改变他们的方向"""
    for enemy in enemys.sprites():
        enemy.rect.y += xz_settings.fleet_drop_speed
    xz_settings.fleet_direction *= -1

def plane_hit(xz_settings,stats,screen,plane,enemys,bullets):
    """响应敌机撞击的飞船"""
    if stats.planes_left > 1:
        # 将planes_left -= 1
        stats.planes_left -= 1

        # 清空敌机列表和子弹列表
        enemys.empty()
        bullets.empty()

        # 创建一群新的敌机，将飞船移动回初始位置
        create_fleet(xz_settings,screen,plane,enemys)
        plane.center_ship()
        
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_enemy_botttom(xz_settings,stats,screen,plane,enemys,bullets):
    """检查是否有敌机到达屏幕底端"""
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            # 像校长被撞一样的处理
            plane_hit(xz_settings,stats,screen,plane,enemys,bullets)
            break

def update_enemys(xz_settings,stats,screen,plane,enemys,bullets):
    """更新敌机的位置"""
    check_fleet_edges(xz_settings,enemys)
    enemys.update()

    # 检测敌机和飞船碰撞
    if pygame.sprite.spritecollideany(plane,enemys):
        print("Plane hit!!!")
        plane_hit(xz_settings,stats,screen,plane,enemys,bullets)
    
    # 检查是否有敌机越界
    check_enemy_botttom(xz_settings,stats,screen,plane,enemys,bullets)
