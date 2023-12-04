import pygame
from setting import *

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # 背景
        self.pre_bg_img = pygame.image.load("shooting/assets/img/background/bg.png") # 画像の読み込み
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_width)) # 画像のサイズを変更
        self.bg_y = 0 # 背景のy座標を初期化
        self.scroll_speed = 0.5 # 背景のスクロールスピード

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height # self.bg_yが0から599までを繰り返す
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height)) # y座標は-600から-1に変化
        self.screen.blit(self.bg_img, (0, self.bg_y)) # 背景の画像を2枚使って、縦スクロールを表現

    def run(self):
        self.scroll_bg()
