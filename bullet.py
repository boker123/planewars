import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):
    """一个飞船发射的子弹进行管理"""

    def __init__(self,xz_settings,screen,plane):
        """在飞船位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen

        # 创建子弹并设置其位置
        self.image = pygame.image.load('images/wsc3.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        self.speed_factor = xz_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        
        # 更新子弹的位置
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        """"在屏幕上绘制子弹"""
        self.screen.blit(self.image,self.rect)
