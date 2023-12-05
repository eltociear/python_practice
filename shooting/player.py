import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups) # classの継承をした際に、親クラスの変数や関数を使用することができる

        # 画像の読み込み
        self.image_list = []
        for i in range(3):
            image = pygame.image.load(f"shooting/assets/img/player/{i}.png") # 　フォルダ内の画像を指定するのにf文字列を使用
            self.image_list.append(image)

        self.index = 0 # 0: 通常時, 1: 左移動, 2: 右移動
        self.pre_image = self.image_list[0] # 画像の初期化
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y)) # 画像の中心座標を(x, y)に設定

        # 移動
        self.direction = pygame.math.Vector2() # 自機が上下左右どこに行くのか判断する変数
        self.speed = 5

    def input(self):
        key = pygame.key.get_pressed() # 押されているキーを取得

        if key[pygame.K_UP]:
            self.direction.y = -1 # pygameのy軸は上がマイナス
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pygame.K_LEFT]:
            self.direction.x = -1 # pygameのx軸は左がマイナス
            self.index = PLAYER_IMG_LEFT # 左移動時の画像に変更
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1 # pygameのx軸は右がプラス
            self.index = PLAYER_IMG_RIGHT # 右移動時の画像に変更
        else:
            self.direction.x = 0
            self.index = PLAYER_IMG_IDLE # 通常時の画像に変更

    # 移動の関数
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction.normalize() # 上下足されてもベクトルの長さを1にする（これが無いと斜め移動が2倍速になる）

        self.rect.x += self.direction.x * self.speed
        self.check_off_screen('horizonal')
        self.rect.y += self.direction.y * self.speed
        self.check_off_screen('vertical')

    # 画面外に出ないようにする関数
    def check_off_screen(self, direction):
        if direction == 'horizonal':
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width

        if direction == 'vertical':
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

    # 画像を更新する関数
    def update_image(self):
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    def update(self):
        self.input()
        self.move()
        self.update_image()