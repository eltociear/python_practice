import pygame
import random
from setting import *

class Block(pygame.sprite.Sprite):
    # ブロックの関数
    def __init__(self, x, y, color, width, height):
        # ブロックの初期化
        pygame.sprite.Sprite.__init__(self)
        # ブロックの大きさを設定
        self.image = pygame.Surface([width, height])
        # ブロックの色を設定
        self.image.fill(color)
        # 画像を囲む四角形
        self.rect = self.image.get_rect()
        # 位置を設定
        self.rect.topleft = (x, y)

class Ellipse(pygame.sprite.Sprite):
    # 楕円のクラス、ドットを楕円で描画するために使用
    def __init__(self, x, y, color, width, height):
        # 楕円の初期化
        pygame.sprite.Sprite.__init__(self)
        # 楕円の大きさを設定
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        # 画像を囲む四角形
        self.rect = self.image.get_rect()
        # 位置を設定
        self.rect.topleft = (x, y)

class Slime(pygame.sprite.Sprite):
    # スライムのクラス
    def __init__(self, x, y, color, width, height):
        # スライムの初期化
        pygame.sprite.Sprite.__init__(self)

        self.change_x = change_x
        self.change_y = change_y

        # 画像を読み込む
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        # 画像を囲む四角形
        self.rect = self.image.get_rect()
        # 位置を設定
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        """
        スライムの移動
        """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        # 画面左端に出た（画像右端の座標が画面左端を出る）場合
        if self.rect.right < 0:
            # 画面右端に移動
            self.rect.left = SCREEN_WIDTH
        # 画面右端に出た（画像左端の座標が画面右端を出る）場合
        elif self.rect.left > SCREEN_WIDTH:
            # 画面左端に移動
            self.rect.right = 0
        # 画面上端に出た（画像下端の座標が画面上端を出る）場合
        if self.rect.bottom < 0:
            # 画面下端に移動
            self.rect.top = SCREEN_HEIGHT
        # 画面下端に出た（画像上端の座標が画面下端を出る）場合
        elif self.rect.top > SCREEN_HEIGHT:
            # 画面上端に移動
            self.rect.bottom = 0

        # 敵がステージのグリッド上のポイントにいたときに以下が実行
        if self.rect.topleft in self.get_intersection_position():
            # 上下左右の移動をランダムに選択
            derection = random.choice(("up", "down", "left", "right"))
            # 左に移動
            if derection == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            # 右に移動
            elif derection == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            # 上に移動
            elif derection == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            # 下に移動
            elif derection == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        # ステージのグリッド上のポイントを取得
        # 行を確認
        for i, row in enumerate(environment()):
            # 列を確認
            for j, item in enumerate(row):
                # ステージで「3」の場合、敵を配置
                if item == 3:
                    items.append((j * 32, i * 32))
        return items

def environment():
    """
    ステージを定義
    """
    grid = ((0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1 ,3, 1, 1, 1, 1, 1 ,3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1 ,3, 1, 1, 1, 1, 1 ,3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1 ,3, 1, 1, 1, 1, 1 ,3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1 ,3, 1, 1, 1, 1, 1 ,3, 1),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0),
            (0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0))
    return grid

def draw_environment(screen):
    for i, row in enumerate(environment()):
        for j, item in enumerate(row):
            # ステージで「1」「2」の場合、線を描画
            if item == 1:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32, i * 32 + 32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)
