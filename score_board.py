# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     score_board
   Description :
   Author :       HoleLin
   date：          2019/4/14
-------------------------------------------------
   Change Activity:
                   2019/4/14:
-------------------------------------------------
"""
import pygame.ftfont
from pygame.sprite import Group
from ship import Ship


class ScoreBoard():
    def __init__(self, ai_settings, screen, status):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.status = status

        # 显示的得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        round_score = int(round(self.status.score, -1))
        scored_str = "{:,}".format(round_score)

        self.score_image = self.font.render(scored_str, True, self.text_color, self.ai_settings.bg_color)
        # 将得分放在屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        round_score = int(round(self.status.score, -1))
        scored_str = "{:,}".format(round_score)

        self.high_score_image = self.font.render(scored_str, True, self.text_color, self.ai_settings.bg_color)
        # 将得分放在屏幕的右上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.status.level), True, self.text_color, self.ai_settings.bg_color)

        # 将等级在得分的下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """显示还剩余多少飞船"""
        self.ships = Group()
        for ship_number in range(self.status.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)