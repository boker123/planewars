import pygame

class Help():
    """储存有关帮助的内容"""
    
    def __init__(self,screen):
        """初始化帮助界面"""
        self.screen = screen

        # 设置返回图标路径，并建模
        self.back_button = pygame.image.load('images/back.png')
        self.back_button_rect = self.back_button.get_rect()
        self.screen_rect = screen.get_rect()
        self.back_button_rect.x = 0
        self.back_button_rect.y = 0

        # 设置帮助界面的文字内容属性
        self.word_color = (30,144,255)
        self.font = pygame.font.SysFont(None,48)
        self.msg1 = "Game Rule"
        self.msg2 = "Control Mode"
        self.msg3 = "Express Gratitude"
        self.delt1 = 400
        self.delt2 = 0
        self.delt3 = -400

        # 图像化文字渲染
        self.msg_image1 = self.font.render(self.msg1,True,self.word_color)
        self.msg_image_rect1 = self.msg_image1.get_rect()
        self.msg_image_rect1.center = self.screen_rect.center
        self.msg_image_rect1.centery = self.screen_rect.centery - self.delt1
        self.msg_image2 = self.font.render(self.msg2,True,self.word_color)
        self.msg_image_rect2 = self.msg_image2.get_rect()
        self.msg_image_rect2.center = self.screen_rect.center
        self.msg_image_rect2.centery = self.screen_rect.centery - self.delt2
        self.msg_image3 = self.font.render(self.msg3,True,self.word_color)
        self.msg_image_rect3 = self.msg_image3.get_rect()
        self.msg_image_rect3.center = self.screen_rect.center
        self.msg_image_rect3.centery = self.screen_rect.centery - self.delt3

        # 帮助的内容
        self.image1 = pygame.image.load('images/EG.png')
        self.image1_rect = self.image1.get_rect()
        self.image1_rect.center = self.screen_rect.center
        self.image1_rect.centery = self.screen_rect.centery + 460

        self.image2 = pygame.image.load('images/GR.png')
        self.image2_rect = self.image2.get_rect()
        self.image2_rect.center = self.screen_rect.center
        self.image2_rect.centery = self.screen_rect.centery - 300

        self.image3 = pygame.image.load('images/CM.png')
        self.image3_rect = self.image2.get_rect()
        self.image3_rect.center = self.screen_rect.center
        self.image3_rect.centery = self.screen_rect.centery + 100


    def back_blitme(self):
        """在指定位置绘制返回按钮"""
        self.screen.blit(self.back_button,self.back_button_rect)

    # def prep_msg(self,msg,delt):
    #     """将msg渲染为图像，并显示"""
    #     self.msg_image = self.font.render(msg,True,self.word_color)
    #     self.msg_image_rect = self.msg_image.get_rect()
    #     self.msg_image_rect.center = self.screen_rect.center
    #     self.msg_image_rect.centery = self.screen_rect.centery - delt

    def draw_help(self):
        """绘制帮助界面"""
        self.screen.blit(self.msg_image1,self.msg_image_rect1)
        self.screen.blit(self.msg_image2,self.msg_image_rect2)
        self.screen.blit(self.msg_image3,self.msg_image_rect3)
        self.screen.blit(self.image1,self.image1_rect)
        self.screen.blit(self.image2,self.image2_rect)
        self.screen.blit(self.image3,self.image3_rect)