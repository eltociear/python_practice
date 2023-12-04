import pygame
from setting import *

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # 背景
        self.pre_bg_img = pygame.image.load("shooting/assets/img/background/bg.png") # 画像の読み込み
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_width)) # 画像のサイズを変更

    def run(self):
        self.screen.blit(self.bg_img, (0, 0))
