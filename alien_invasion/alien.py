import pygame
from pygame.sprite import Sprite
import random




class Alien(Sprite):
    """表示单个外星人类"""
    def __init__(self, ai_settings, screen, random_rect):
        super().__init__()
        self.props_time = random.random() - ai_settings.prop_time
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = int((ai_settings.screen_width - (self.rect.right - self.rect.left)) * random_rect)
        self.rect.y = 0
        # 利用浮点数来精确控制位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_move = random.random() - 0.5
        self.left_key = False
        self.right_key = False

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_key(self):
        """检测是否到边缘"""
        if not self.left_key and not self.right_key:
            if self.x_move >= 0:
                self.right_key = True
            else:
                self.left_key = True
        elif self.left_key and (self.x - self.ai_settings.alien_move_speed_x) < 0:
            self.right_key = True
            self.left_key = False
        elif self.right_key and (self.rect.right + self.ai_settings.alien_move_speed_x) > self.screen_rect.right:
            self.left_key = True
            self.right_key = False



    def update(self):
        """更新外星人位置"""
        self.y += self.ai_settings.alien_move_speed_y
        self.rect.y = int(self.y)
        self.check_key()
        # 随机移动
        if self.left_key:
            self.x -= self.ai_settings.alien_move_speed_x
            self.rect.x = int(self.x)
        elif self.right_key:
            self.x += self.ai_settings.alien_move_speed_x
            self.rect.x = int(self.x)
        
        


