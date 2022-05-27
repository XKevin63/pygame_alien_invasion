class Settings():

    def __init__(self):
        """系统设置类"""
        # 背景设置
        self.aviliable = True
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        # 飞船设置
        self.ship_speed = 2
        self.max_live = 3
        # 子弹类设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.max_bullets = 8
        # 外星人设置
        self.alien_add_time = 3
        self.alien_move_speed_y = 0.2
        self.alien_move_speed_x = 0.5
        self.alien_max_number = 5
        # 道具设置
        self.prop_speed_x = 0.5
        self.prop_speed_y = 0.5
        self.prop_time = 0.3




    