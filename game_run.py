import pygame

from pygame.locals import *
from settings import Settings
from plane import Plane
from enemy import Enemy
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
import game_functions as gf


def rungame():
    """运行游戏的主函数"""

    # 创建一个游戏窗口
    pygame.init()

    # 设置窗口大小和游戏名称
    xz_settings = Settings()
    screen = pygame.display.set_mode((xz_settings.screen_width,xz_settings.screen_height))
    pygame.display.set_caption("校长的热狗-v1.0")

    # 创建Play按钮
    play_button = Button(xz_settings,screen,"Play")
    # 创建用于统计游戏信息的实例
    stats = GameStats(xz_settings)

    # 创建飞机模型
    plane = Plane(screen)

    # 创建一个储存子弹的编组
    bullets = Group()
    enemys = Group()

    # 创建一群敌机
    gf.create_fleet(xz_settings,screen,plane,enemys)

    # 游戏的主循环
    while True:
        # pygame.display.update()
        
        # 响应事件
        gf.check_events(xz_settings,screen,stats,play_button,plane,enemys,bullets)
        if stats.game_active:
                # 射击子弹
                gf.update_bullets(xz_settings,screen,plane,enemys,bullets)

                # 移动敌机
                gf.update_enemys(xz_settings,stats,screen,plane,enemys,bullets)

        # 绘制屏幕
        gf.update_screen(xz_settings,stats,screen,plane,enemys,bullets,play_button)

# 运行游戏
if __name__ == "__main__":
    rungame()