import pygame
from setting import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups) # classの継承をした際に、親クラスの変数や関数を使用することができる

        # 画像の読み込み
        self.image_list = []
        for i in range(2):
            image = pygame.image.load(f"shooting/assets/img/bullet/{i}.png") # 　フォルダ内の画像を指定するのにf文字列を使用
            self.image_list.append(image)

        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (24, 48))
        self.rect = self.image.get_rect(midbottom=(x, y)) #center(中心)を(x, y)に設定

        # 移動
        self.speed = BULLET_SPEED

    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill() # 自分自身をグループから削除

    # 画像のアニメーションの関数
    def animation(self):
        self.index += 0.5

        if self.index >= len(self.image_list):
            self.index = 0

        self.pre_image = self.image_list[int(self.index)]
        self.image = pygame.transform.scale(self.pre_image, (24, 48))

    # 移動の関数
    def move(self):
        self.rect.y -= self.speed

    def update(self):
        self.move()
        self.check_off_screen()
        self.animation()
