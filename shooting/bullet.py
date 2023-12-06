import pygame
from setting import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups) # classの継承をした際に、親クラスの変数や関数を使用することができる

        # 画像の読み込み
        self.image = pygame.Surface((10, 30))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect(midbottom=(x, y)) #center(中心)を(x, y)に設定

        # 移動
        self.speed = BULLET_SPEED

    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill() # 自分自身をグループから削除

    # 移動の関数
    def move(self):
        self.rect.y -= self.speed

    def update(self):
        self.move()
        self.check_off_screen()
