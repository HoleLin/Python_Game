# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Ship
   Description :
   Author :       HoleLin
   date：          2019/4/11
-------------------------------------------------
   Change Activity:
                   2019/4/11:
-------------------------------------------------
"""
import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设置移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blit_ship(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        # 移动标志位True 且 在正确活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def ship_center(self):
        """让飞船在屏幕居中"""
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom