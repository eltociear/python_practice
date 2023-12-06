import pygame
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        # 画像の読み込み
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))

        # 移動
        self.direction = pygame.math.Vector2(0, 1) # 最初の数字がx方向、2番目の数字がy方向（デフォルトは0, 0）
        self.speed = 1

    def move(self):
        self.rect.y += self.direction.y * self.speed

    def update(self):
        self.move()
