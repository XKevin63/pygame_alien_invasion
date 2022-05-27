import pygame


class Button():
    """按钮类"""
    def __init__(self, screen):
        """初始化按钮"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮的rect对象，并其剧中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只要创建一次
        self.msg = 'play again'
        self.preg_msg()


    def preg_msg(self):
        """将msg渲染为图像，并使其剧中"""
        # True为开启反锯齿
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.display.flip()

