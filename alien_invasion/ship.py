import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类，包含飞船的信息"""

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/ship.png')
        self.speed = ai_settings.ship_speed
        self.live = 1
        self.live_image = pygame.image.load('images/live.png')
        
        # 获取屏幕矩形信息,船图像信息和生命图像
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.live_rect = self.live_image.get_rect()

        # 将飞船定位在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        
        # 飞船移动标志信号
        self.moving_right = False
        self.moving_left = False



    def live_blitme(self):
        """判断各个生命位置"""
        for number in range(0,self.live):
            self.live_rect.right = self.screen_rect.right - number * (self.live_rect.right - self.live_rect.left)
            self.screen.blit(self.live_image, self.live_rect)




    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)
        self.live_blitme()

    
    def update(self):
        """更新飞船位置"""
        # 控制飞船不会超出屏幕外
        if self.moving_left and self.rect.left >= (self.screen_rect.left + self.speed):
            self.center -= self.speed
        if self.moving_right and self.rect.right <= (self.screen_rect.right - self.speed):
            self.center += self.speed

        self.rect.centerx = int(self.center)

    def to_orgin(self):
        """飞船回到初始位置"""
        self.live = 1
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False




    



