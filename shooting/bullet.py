import pygame
from setting import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups) # classの継承をした際に、親クラスの変数や関数を使用することができる

        # 画像の読み込み
        self.image = pygame.Surface((10, 30))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect(center=(x, y)) #center(中心)を(x, y)に設定

    def update(self):
        pass # 今回は何もしない
