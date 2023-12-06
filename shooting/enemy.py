import pygame
import random
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        # 画像の読み込み
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))

        # 移動
        move_list = [1, -1]
        self.direction = pygame.math.Vector2(random.choice(move_list), 1) # 最初の数字がx方向、2番目の数字がy方向（デフォルトは0, 0）、move_listからランダムに選択
        self.speed = 1
        self.timer = 0

    def move(self):
        # ジグザグに折り返しさせる
        self.timer += 1
        if self.timer >= 80:
            self.direction.x *= -1
            self.timer = 0

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    # 画面外に出たら消える
    def check_off_screen(self):
        if self.rect.top > screen_height:
            self.kill()

    def update(self):
        self.move()
        self.check_off_screen()
