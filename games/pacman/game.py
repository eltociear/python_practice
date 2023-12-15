import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox # メッセージボックスに必要
from setting import *
import os

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
        self.player = Player(32, 128, PLAYER_IMAGE)

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
        for event in pygame.event.get():
            # QUIT状態になったらゲームを終了
            if event.type == pygame.QUIT:
                return True

            # メニュー操作
            self.menu.event_handler(event)
            # キー判定
            if event.type == pygame.KEYDOWN:
                # ENTERキーが押されたら
                if event.key == pygame.K_RETURN:
                    # ゲームオーバー状態かつaboutフラグがFalseの場合
                    if self.game_over and not self.about:
                        # Start Gameが選択されている場合
                        if self.menu.state == 0:
                            # 初期化
                            self.__init__()
                            # ゲームオーバーフラグをFalseにする
                            self.game_over = False
                        # Aboutが選択されている場合
                        elif self.menu.state == 1:
                            # aboutフラグをTrueにする
                            self.about = True
                        # Quitが選択されている場合
                        elif self.menu.state == 2:
                            # ゲームを終了
                            return True
                # 右矢印キーが押されたら
                elif event.key == pygame.K_RIGHT:
                    # プレイヤーを右に移動
                    self.player.move_right()
                # 左矢印キーが押されたら
                elif event.key == pygame.K_LEFT:
                    # プレイヤーを左に移動
                    self.player.move_left()
                # 上矢印キーが押されたら
                elif event.key == pygame.K_UP:
                    # プレイヤーを上に移動
                    self.player.move_up()
                # 下矢印キーが押されたら
                elif event.key == pygame.K_DOWN:
                    # プレイヤーを下に移動
                    self.player.move_down()
                # ESCキーが押されたら
                elif event.key == pygame.K_ESCAPE:
                    # ゲームオーバーフラグをTrueにする
                    self.game_over = True
                    # aboutフラグをFalseにする
                    self.about = False
            # キーが離されたら
            elif event.type == pygame.KEYUP:
                # 右矢印キーが離されたら
                if event.key == pygame.K_RIGHT:
                    # 右移動を停止
                    self.player.stop_move_right()
                # 左矢印キーが離されたら
                elif event.key == pygame.K_LEFT:
                    # 左移動を停止
                    self.player.stop_move_left()
                # 上矢印キーが離されたら
                elif event.key == pygame.K_UP:
                    # 上移動を停止
                    self.player.stop_move_up()
                # 下矢印キーが離されたら
                elif event.key == pygame.K_DOWN:
                    # 下移動を停止
                    self.player.stop_move_down()
        return False

    def run_logic(self):
        # ゲームオーバー状態でない場合
        if not self.game_over:
            # プレイヤーを移動
            self.player.update(self.horizontal_blocks, self.vertical_blocks)
            # プレイヤーとドットの衝突判定
            block_hit_list = pygame.sprite.spritecollide(self.player, self.dots_group, True)
            # 衝突した場合
            if len(block_hit_list) > 0:
                # スコアを加算
                self.score += 1

            # プレイヤーと敵の衝突判定
            block_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, True)
            # 衝突した場合
            if len(block_hit_list) > 0:
                # プレイヤーの爆発フラグをTrueにする
                self.player.explosion = True

            # ゲームオーバーフラグをTrueにする
            self.game_over = self.player.game_over
            # 敵をupdate
            self.enemies.update(self.horizontal_blocks, self.vertical_blocks)

    def display_frame(self, screen):
        """
        画面描画を管理
        """
        # 画面を黒色で塗りつぶす
        screen.fill(BLACK)

        # ゲームオーバー状態の場合
        if self.game_over:
            # aboutを選択している場合
            if self.about:
                # aboutを表示
                self.display_message(screen, "PACMAN like dot ear game made by: @eltociear", BLUE)
            else:
                # メニューを表示
                self.menu.display_frame(screen)
        else:
            # 水平方向のブロックを描画
            self.horizontal_blocks.draw(screen)
            # 垂直方向のブロックを描画
            self.vertical_blocks.draw(screen)
            # その他の環境を描画
            draw_environment(screen)
            # ドットを描画
            self.dots_group.draw(screen)
            # 敵を描画
            self.enemies.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            # スコアを表示
            text = self.font.render("Score: {}".format(self.score), True, GREEN)

        pygame.display.flip()

    def display_message(self, screen, message, color = (255, 0, 0)):
        """
        メッセージを表示
        """
        # メッセージを表示
        label = self.font.render(message, True, color)

        width = label.get_width()
        height = label.get_height()

        posX = (SCREEN_WIDTH / 2) - (width / 2)
        posY = (SCREEN_HEIGHT / 2) - (height / 2)

        screen.blit(label, (posX, posY))

class Menu(object):
    """
    メニューを作成するクラス
    """
    # メニューのインデックス
    state = 0
    def __init__(self, items, font_color = (0, 0, 0), select_color = (255, 0, 0), ttf_font = None, font_size = 25):
        # デフォルトのテキストカラー
        self.font_color = font_color
        # 選択時のテキストカラー
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

    def display_frame(self, screen):
        """
        メニューのテキストを選択するときの色を変更
        """
        for index, item in enumerate(self.items):
            if self.state == index:
                # 選択時の色
                label = self.font.render(item, True, self.select_color)
            else:
                # デフォルトの色
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH / 2) - (width / 2)
            # t_h: テキストの高さ
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))

    def event_handler(self, event):
        """
        メニュー操作
        """
        # キーが押されたら
        if event.type == pygame.KEYDOWN:
            # 上矢印キーが押されたら
            if event.key == pygame.K_UP:
                if self.state > 0:
                    # 上に移動
                    self.state -= 1
            # 下矢印キーが押されたら
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) - 1:
                    # 下に移動
                    self.state += 1
