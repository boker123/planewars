import sys
import pygame
from bullet import Bullet

def check_events(xz_settings,screen,plane,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            # 用点击空格射击子弹
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_bullet(xz_settings,screen,plane,bullets)
                
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

def update_screen(xz_settings,screen,plane,bullets):
    """ 更新屏幕上的图像，并且切换到屏幕"""

    # 绘制屏幕添加底色和背景图
    screen.fill(xz_settings.bg_color)
    screen.blit(xz_settings.bg_img,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，删除消失的子弹"""

    # 更新子弹的位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                    bullets.remove(bullets)
    print(len(bullets))

def fire_bullet(xz_settings,screen,plane,bullets):
    """射击子弹"""
    print("SPACE")
    if len(bullets) < xz_settings.bullets_allowed:
        new_bullet = Bullet(xz_settings,screen,plane)
        bullets.add(new_bullet)