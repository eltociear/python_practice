import pygame
from setting import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        # 画像
        self.image_list = []
        for i in range(5):
            image = pygame.image.load(f"shooting/assets/img/explosion/{i}.png")
            self.image_list.append(image)

        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y)) # 画像の中心座標を(x, y)に設定

    def animation(self):
        self.index += 0.2
        if self.index < len(self.image_list):
            self.pre_image = self.image_list[int(self.index)]
            self.image = pygame.transform.scale(self.pre_image, (50, 50))
        else:
            self.kill()

    def update(self):
        self.animation()
