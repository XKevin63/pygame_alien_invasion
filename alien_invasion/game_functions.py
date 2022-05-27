import sys
import time
import pygame
import random

from bullet import Bullet
from alien import Alien
from boom import Boom
from prop import prop




def keydown_events(event, ai_settings, screen, ship, bullets):
    """响应键盘按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def keyup_events(event, ship):
    """响应键盘抬起"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event,ship)

            


def update_screen(ai_settings, screen, ship, bullets, aliens, booms, props):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    for alien in aliens:
        alien.blitme()
    for boom in booms:
        boom.blitme()
    for prop in props:
        prop.blitme()
    ship.blitme()
    # 绘制新屏幕
    pygame.display.flip()

def ship_collide_check(ships, aliens, ai_setting):
    collisions = pygame.sprite.groupcollide(ships, aliens, False, True)
    if len(collisions) > 0:
        for ship in ships:
            if ship.live > 1:
                ship.live -= 1
            else:
                ai_setting.aviliable = False


def alien_check(aliens, ships, ai_setting):
    """检测外星人是否超出屏幕"""
    ship_collide_check(ships, aliens, ai_setting)
    for alien in aliens.copy():
        if alien.rect.top >= alien.screen_rect.bottom:
            aliens.remove(alien)
    print("剩余外星人数：" + str(len(aliens)))



def bullet_check(bullets, aliens, booms, props, screen, ai_setting):
    """检测子弹是否超出屏幕"""
    collide_check(bullets, aliens, booms, props, screen, ai_setting)
    # 列表中不应删除，使用copy
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print("剩余子弹数：" + str(len(bullets)))


def collide_check(bullets, aliens, booms, props, screen, ai_settings):
    """碰撞检测"""
    # True代表对应物体碰撞后是否删除
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for bullet in collisions:
        alien_s = collisions[bullet]
        for alien in alien_s:
            boom_create(alien, booms)
            if alien.props_time < 0:
                # 随机选择道具种类
                prop_chose = random.randint(1,2)
                new_prop = prop(alien, screen, ai_settings, prop_chose)
                props.add(new_prop)
                



def boom_create(alien, booms):
    """爆炸效果展示"""
    new_boom = Boom(alien)
    booms.add(new_boom)

def boom_check(booms):
    """检查爆炸效果时间"""
    for boom in booms.copy():
        now_time = time.perf_counter()
        during_time = now_time - boom.create_time
        if during_time > 1:
            booms.remove(boom)




def game_updata(ship, bullets, aliens, props):
    ship.update()
    bullets.update()
    aliens.update()
    props.update()


def alien_add(pre_time, aliens, ai_settings, screen):
    """定时添加外星人"""
    now_time = time.perf_counter()
    scond = now_time - pre_time
    if len(aliens) < ai_settings.alien_max_number and scond > ai_settings.alien_add_time:
        random_ract = random.random()
        new_alien = Alien(ai_settings, screen, random_ract)
        aliens.add(new_alien)
    
    if scond > ai_settings.alien_add_time:
        return now_time
    else:
        return pre_time


    
def button_event_check(button, ai_setting, bullets, aliens, booms, ships, props, ship, game_state):
    """检测是否按下按钮"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(button, mouse_x, mouse_y, ai_setting, bullets, aliens, booms, ships, ship, game_state, props)
        


def check_play_button(button, mouse_x, mouse_y, ai_setting, bullets, aliens, booms, ships, ship, game_state, props):
    """判断是否是按下按钮"""
    if button.rect.collidepoint(mouse_x, mouse_y):
        ai_setting.aviliable = True
        game_state.to_orgin(bullets, aliens, booms)
        ships.empty()
        props.empty()
        ship.to_orgin()
        ships.add(ship)




def prop_check(ships, props, ai_setting):
    """检测是否吃到道具"""
    prop_exit(props)
    collision = pygame.sprite.groupcollide(props, ships, True, False)
    for propk in collision:
        for ship in ships:
            if propk.chose == 1 and ship.live < ai_setting.max_live:
                ship.live += 1
            elif propk.chose == 2 and ai_setting.bullets_allowed < ai_setting.max_bullets:
                ai_setting.bullets_allowed += 1




def prop_exit(props):
    """检测道具是否超出屏幕"""
    for prop in props:
        if prop.rect.top >= prop.screen_rect.bottom:
            props.remove(prop)
