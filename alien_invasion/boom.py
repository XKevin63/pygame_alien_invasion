import pygame
from pygame.sprite import Sprite
import time



class Boom(Sprite):
    """爆炸效果展示类"""
    def __init__(self, alien):
        super().__init__()
        self.screen = alien.screen
        self.image = pygame.image.load('images/boom.png')
        self.rect = self.image.get_rect()
        self.rect.x = alien.rect.x
        self.rect.y = alien.rect.y
        self.create_time = time.perf_counter()

    
    def blitme(self):
        """绘制爆炸图像"""
        self.screen.blit(self.image, self.rect)