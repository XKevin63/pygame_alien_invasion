from pygame.sprite import Sprite
import pygame
import random



class prop(Sprite):
    """加生命的道具"""
    def __init__(self, alien, screen, ai_settings, chose=1):
        super().__init__()
        self.screen = screen
        self.chose = chose
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/live_yao.png')
        self.image_chose()
        self.rect = self.image.get_rect()
        self.rect.x = alien.rect.x
        self.rect.y = alien.rect.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_move = random.random() - 0.5
        self.left_key = False
        self.right_key = False
    
    def image_chose(self):
        """选则道具类型"""
        if self.chose == 1:
            self.image = pygame.image.load('images/live_yao.png')
        elif self.chose == 2:
            self.image = pygame.image.load('images/strong_yao.png')



    def blitme(self):
        """绘制道具"""
        self.screen.blit(self.image, self.rect)


    def check_key(self):
        """检测是否到边缘"""
        if not self.left_key and not self.right_key:
            if self.x_move >= 0:
                self.right_key = True
            else:
                self.left_key = True
        elif self.left_key and (self.x - self.ai_settings.prop_speed_x) < 0:
            self.right_key = True
            self.left_key = False
        elif self.right_key and (self.rect.right + self.ai_settings.prop_speed_x) > self.screen_rect.right:
            self.left_key = True
            self.right_key = False



    def update(self):
        """更新位置"""
        self.y += self.ai_settings.prop_speed_y
        self.rect.y = int(self.y)
        self.check_key()
        # 随机移动
        if self.left_key:
            self.x -= self.ai_settings.prop_speed_x
            self.rect.x = int(self.x)
        elif self.right_key:
            self.x += self.ai_settings.prop_speed_x
            self.rect.x = int(self.x)