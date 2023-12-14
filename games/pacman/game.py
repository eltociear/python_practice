import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox # メッセージボックスに必要

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Game(object):
    """
    ゲームクラス
    """
    def __init__(self):
        """
        クラス初期化
        """
        # fontの初期化
        self.font = pygame.font.Font(None, 40)
        # aboutフラグ
        self.about = False
        # ゲームオーバーフラグ
        self.game_over = True
        # スコア
        self.score = 0
        # フォント
        self.font = pygame.font.Font(None, 35)

        # メニューを設定。後述のMenuクラスを初期化
        self.menu = Menu(("Start Game", "About", "Quit"), font_color=WHITE, font_size=60)
        # プレイヤーを初期化
        self.player = Player(32, 128, 'player.png')

        # 水平ブロック
        self.horizontal_blocks = pygame.sprite.Group()
        # 垂直ブロック
        self.vertical_blocks = pygame.sprite.Group()

        # ドットのグループ
        self.dots_group = pygame.sprite.Group()

        # ブロックの描画
        for i, row in enumerate(environment()):
            for j, item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))

        # 敵の定義
        self.enemies = pygame.sprite.Group()
        # 敵を追加。初期位置と移動座標を引数に渡す
        self.enemies.add(Slime(288, 96, 0, 2))
        self.enemies.add(Slime(288, 320, 0, -2))
        self.enemies.add(Slime(544, 128, 0, 2))
        self.enemies.add(Slime(32, 224, 0, 2))
        self.enemies.add(Slime(160, 64, 2, 0))
        self.enemies.add(Slime(448, 64, -2, 0))
        self.enemies.add(Slime(640, 448, 2, 0))
        self.enemies.add(Slime(448, 320, 2, 0))

        # ドットを追加
        for i, row in enumerate(environment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))

    def process_events(self):
        """
        キー操作
        """
