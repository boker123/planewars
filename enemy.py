import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """表示单位敌机的类"""

    def __init__(self,xz_settings,seat,screen):
        """初始化外新人设置初始位置"""
        super(Enemy,self).__init__()
        self.screen = screen
        self.xz_settings = xz_settings

        # 加载敌机图像，设置rect值
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()

        # 设置外星人初始的位置
        self.rect.topleft = seat

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        """如果敌机到达边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """向右移动外新人"""
        self.rect.x += (self.xz_settings.enemy_speed_factor * self.xz_settings.fleet_direction)
        self.rect.y += self.xz_settings.fleet_drop_speed
    
    

