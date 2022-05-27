import time
import pygame
from pygame.sprite import Group

import game_functions as gf
from setting import Settings
from ship import Ship
from game_state import GameStates
from button import Button


        

def run_game():
    """游戏运行"""
    # 初始化游戏参数
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_setting)
    play_game = Button(screen)
    # 管理的编组
    bullets = Group()
    aliens = Group()
    booms = Group()
    ships = Group()
    props = Group()
    game_state = GameStates()
    ships.add(ship)

    while True:
        gf.button_event_check(play_game, ai_setting, bullets, aliens, booms, ships, props, ship, game_state)
        now_time = time.perf_counter()
        while ai_setting.aviliable:
            gf.check_events(ai_setting, screen, ship, bullets)
            gf.game_updata(ship, bullets, aliens, props)
            gf.bullet_check(bullets, aliens, booms, props, screen, ai_setting)
            gf.boom_check(booms)
            gf.alien_check(aliens, ships, ai_setting)
            gf.prop_check(ships, props, ai_setting)
            now_time = gf.alien_add(now_time, aliens, ai_setting, screen)
            gf.update_screen(ai_setting, screen, ship, bullets, aliens, booms, props)
        play_game.draw_button()
        

run_game()
