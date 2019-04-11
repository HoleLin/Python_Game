# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     game_functions
   Description :    游戏方法模块 -- 游戏所有方法
   Author :       HoleLin
   date：          2019/4/11
-------------------------------------------------
   Change Activity:
                   2019/4/11:
-------------------------------------------------
"""
import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)


def chek_keyup_events(event, ship):
    """ 响应松开 """
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 响应按下 """
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    """ 如果没到达限制,就发射一颗子弹 """
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一颗子弹,并将其加入到编组bullets中
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)


def update_screen(ai_setting, screen, ship, alien, bullets):
    """ 更新屏幕上的图像,并且换到新屏幕 """
    # 每次循环是都重绘屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blit_ship()
    alien.blit_alien()
    # 让最近的绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
