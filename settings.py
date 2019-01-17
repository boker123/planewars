import pygame

# 背景初始化设置
class Settings():
    """"储存校长的面包的所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.bg_img = pygame.image.load('images/bg.jpg')

        # 校长的设置
        self.plane_speed_factor = 3

        # 子弹的设置
        self.bullet_speed_factor = 5
        self.bullets_allowed = 6
