import pygame.font
from pygame.sprite import Group

from plane import Plane

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self,xz_settings,screen,stats):
        """初始化显示得分信息的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.xz_settings = xz_settings
        self.stats = stats

        # 显示得分信息用的字体
        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont(None,48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_level()
        self.prep_plane()

    def prep_score(self):
        """将得分转化为图像"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.xz_settings)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """将等级渲染为图像"""
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.xz_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_plane(self):
        """显示剩余生命值"""
        self.planes = Group()
        for plane_number in range(self.stats.planes_left):
            plane = Plane(self.xz_settings,self.screen)
            plane.rect.x = 10 + plane_number * plane.rect.width
            plane.rect.y = 10
            self.planes.add(plane)



    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.planes.draw(self.screen)

    