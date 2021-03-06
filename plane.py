import pygame
from pygame.sprite import Sprite

# 创建飞机模型
class Plane(Sprite):
    def __init__(self,xz_settings,screen):
        """初始化飞机设置其初始位置"""
        super(Plane,self).__init__()
        self.screen = screen

        # 加载飞船图像获取其外接矩形
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image,self.rect)

    def center_plane(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom