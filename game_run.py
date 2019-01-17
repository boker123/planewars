import pygame

from pygame.locals import *
from settings import Settings
from plane import Plane
from pygame.sprite import Group
import game_functions as gf


def rungame():
    """运行游戏的主函数"""

    # 创建一个游戏窗口
    pygame.init()

    # 设置窗口大小和游戏名称
    xz_settings = Settings()
    screen = pygame.display.set_mode((xz_settings.screen_width,xz_settings.screen_height))
    pygame.display.set_caption("校长的热狗")
    
    # 创建飞机模型
    plane = Plane(screen)

    # 创建一个储存子弹的编组
    bullets = Group()

    while True:
        # pygame.display.update()

        # 响应事件
        gf.check_events(xz_settings,screen,plane,bullets)

        # 射击子弹
        gf.update_bullets(bullets)

        # 绘制屏幕
        gf.update_screen(xz_settings,screen,plane,bullets)



# 运行游戏
if __name__ == "__main__":
    rungame()