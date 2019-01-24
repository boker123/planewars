import pygame

# 背景初始化设置
class Settings():
    """"储存校长的面包的所有设置"""

    def __init__(self):
        """初始化游戏静态设置"""
        self.time = 0
        # 屏幕设置
        self.bg_color = (135,206,250)
        self.bg_img = pygame.image.load('images/bg5.jpg')
        self.bg_img2 = pygame.image.load('images/bg55.jpg')
        self.bg_img_rect = self.bg_img.get_rect()
        self.bg_img2_rect = self.bg_img2.get_rect()
        self.bg_img_rect.y = 0
        self.bg_img2_rect.y = -self.bg_img2_rect.height
        self.screen_width = self.bg_img_rect.width
        self.screen_height = self.bg_img_rect.height

        self.screen_speed = 1

        # 校长的设置
        self.plane_speed_factor = 3
        self.plane_health = 3

        # 子弹的设置
        self.bullet_speed_factor = 5
        self.bullets_allowed = 12

        # 敌机的设置
        self.enemy_speed_factor = 1
        self.fleet_drop_speed = 1
        self.enemys_sum = 10
        # 控制左右移 1为右移,-1为左移
        self.fleet_direction = 1
        self.come_time = 80

        # 节奏加快的方式
        self.speedup_scale = 1.1
        # 点数提高的方式
        self.score_scale = 1.5
        # 提高等级的方式
        self.level_scale = 200

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏变化的设置"""
        self.plane_speed_factor = 3
        self.bullet_speed_factor = 5
        self.enemy_speed_factor = 1

        self.fleet_direction = 1

        self.enemy_points = 50
    
    def increase_speed(self):
        """提高速度"""
        self.plane_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)

    def reaction(self):
        self.bg_img_rect.y += self.screen_speed
        self.bg_img2_rect.y += self.screen_speed
        if self.bg_img_rect.y >= self.bg_img_rect.height:
            self.bg_img_rect.y = -self.bg_img_rect.height
        if self.bg_img2_rect.y >= self.bg_img2_rect.height:
            self.bg_img2_rect.y = -self.bg_img2_rect.height