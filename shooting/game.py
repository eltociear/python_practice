import pygame
import random
from setting import *
from player import Player
from enemy import Enemy
from support import draw_text

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        # グループの作成
        self.create_group()

        # 自機
        self.player = Player(self.player_group, 300, 500, self.enemy_group) # selfをつけるとクラス内のどこでも使える変数になる

        # 敵
        self.timer = 0 # 敵を作成するタイミングを管理するタイマー

        # 背景
        self.pre_bg_img = pygame.image.load("shooting/assets/img/background/bg.png") # 画像の読み込み
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_width)) # 画像のサイズを変更
        self.bg_y = 0 # 背景のy座標を初期化
        self.scroll_speed = 0.5 # 背景のスクロールスピード

        # ゲームオーバー
        self.game_over = False

        # BGM
        # pygame.mixer.music.load("shooting/assets/sound/bgm.mp3")
        # pygame.mixer.music.play(-1) # -1を指定するとループ再生
        # pygame.mixer.music.set_volume(0.3) # 音量の設定

    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle() # 1体のプレイヤーを管理するグループ
        self.enemy_group = pygame.sprite.Group() # 敵を管理するグループ

    # 敵を作成する関数
    def create_enemy(self):
        self.timer += 1
        if self.timer >= 50:
            enemy = Enemy(self.enemy_group, random.randint(50, 550), 0, self.player.bullet_group) # 敵を作成 50から550の間でランダムにx座標を決定
            self.timer = 0

    def player_death(self):
        if len(self.player_group) == 0:
            self.game_over = True
            draw_text(self.screen, "GAME OVER", screen_width // 2, screen_height // 2, 75, RED)
            draw_text(self.screen, "press SPACE KEY to reset", screen_width // 2, screen_height // 2 + 100, 50, RED)

    def reset(self):
        key = pygame.key.get_pressed()
        if self.game_over and key[pygame.K_SPACE]:
            self.create_group()
            self.player = Player(self.player_group, 300, 500, self.enemy_group)
            self.enemy_group.empty() # 空にしておかないと復活の瞬間に再度ゲームオーバーになってしまう
            self.game_over = False

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height # self.bg_yが0から599までを繰り返す
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height)) # y座標は-600から-1に変化
        self.screen.blit(self.bg_img, (0, self.bg_y)) # 背景の画像を2枚使って、縦スクロールを表現

    def run(self):
        self.scroll_bg()

        self.create_enemy()

        # グループの描画と更新
        self.player_group.draw(self.screen) # Game内のself.screenに描画
        self.player_group.update()
        self.enemy_group.draw(self.screen) # Game内のself.screenに描画
        self.enemy_group.update()
        self.player_death()
        self.reset()
