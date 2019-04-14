"""
-------------------------------------------------
   File Name：     alien_invasion.py
   Description :   外星人入侵主类
   Author :       HoleLin
   date：          2019/4/11
-------------------------------------------------
   Change Activity:
                   2019/4/11:
-------------------------------------------------
"""
import pygame

import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_status import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置对象
    ai_settings = Setting()

    # 设置一个长为1200,宽为800的窗口
    # pygame.display.set_mode.() 参数为元祖
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 创建一群外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建用于存储游戏统计信息的实例
    status = GameStats(ai_settings)
    # 创建存储游戏统计信息的实例,并创建记分牌
    sb = ScoreBoard(ai_settings, screen, status)
    # 开始游戏的主循环
    while True:
        # 检查退出
        gf.check_events(ai_settings, screen, sb, status, play_button, ship, aliens, bullets)
        if status.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, status, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, status, sb, screen, ship, aliens, bullets)
        # 刷新屏幕
        gf.update_screen(ai_settings, status, sb, screen, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
