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
