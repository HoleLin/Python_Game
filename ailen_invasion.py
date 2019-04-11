import sys
import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置一个长为1200,宽为800的窗口
    # pygame.display.set_mode.() 参数为元祖
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近的绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
