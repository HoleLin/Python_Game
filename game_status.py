# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     game_status
   Description :
   Author :       HoleLin
   date：          2019/4/12
-------------------------------------------------
   Change Activity:
                   2019/4/12:
-------------------------------------------------
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_setting = ai_settings
        self.reset_status()
        # 游戏刚启动是处于活动状态
        self.game_active = True

    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_setting.ship_limit
