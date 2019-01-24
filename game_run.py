import pygame

from pygame.locals import *
from settings import Settings
from plane import Plane
from enemy import Enemy
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group
from game_stats import GameStats
from helpset import Help
import game_functions as gf


def rungame():
    """运行游戏的主函数"""

    # 创建一个游戏窗口
    pygame.init()

    # 设置窗口大小和游戏名称
    xz_settings = Settings()
    screen = pygame.display.set_mode((xz_settings.screen_width,xz_settings.screen_height))
    pygame.display.set_caption("星球大战-v0.1（内测）")

    # 创建开始前的背景音乐
    pygame.mixer.music.load("sounds/bgm3.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    pygame.mixer.music.set_volume(0.2)

    # 创建音效
    enemy_down = pygame.mixer.Sound("sounds/enemy2_down.wav")
    bullet_sound = pygame.mixer.Sound("sounds/bullet.wav")

    # 创建Play按钮
    play_button = Button(xz_settings,screen,"Play",200)
    help_button = Button(xz_settings,screen,"Help",100)
    exit_button = Button(xz_settings,screen,"Exit",0)

    # 创建用于统计游戏信息的实例，和帮助界面
    stats = GameStats(xz_settings)
    helpset = Help(screen)

    # 创建记分牌
    sb = Scoreboard(xz_settings,screen,stats)

    # 创建飞机模型
    plane = Plane(xz_settings,screen)

    # 创建一个储存子弹的编组
    bullets = Group()
    enemys = Group()

    # 游戏的主循环
    while True:
        
        # print(xz_settings.time)
        # 响应事件
        gf.check_events(xz_settings,screen,stats,sb,play_button,help_button,exit_button,plane,enemys,bullets,helpset,bullet_sound)
        if stats.game_active:
                # 记录循环次数
                xz_settings.time = (xz_settings.time + 1) % xz_settings.come_time
                
                # 射击子弹
                gf.update_bullets(xz_settings,screen,stats,sb,plane,enemys,bullets,enemy_down)

                # 移动敌机
                gf.update_enemys(xz_settings,stats,sb,screen,plane,enemys,bullets)
                

        # 绘制屏幕
        gf.update_screen(xz_settings,stats,sb,screen,plane,enemys,bullets,helpset,play_button,help_button,exit_button)

# 运行游戏
if __name__ == "__main__":
    rungame()