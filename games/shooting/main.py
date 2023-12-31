# -*- coding: utf-8 -*-
import pygame
from setting import * # *と打つと対象ファイルの全ての変数と関数を読み込む
from game import Game

pygame.mixier.init() # 音声ファイルを使用する場合は必ず記述、これがないとバグやエラーが発生する
pygame.init() # pygameの初期化しないとエラーになる

# ウインドウの作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# FPSの設定
clock = pygame.time.Clock()

# ゲーム
game = Game()

# メインループ =============================================================
run = True
while run:
    # 背景の描画
    screen.fill(BLACK)

    # ゲームの実行
    game.run()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # 画面の更新
    pygame.display.update() # 何か処理をした場合、必ず画面を更新する
    clock.tick(FPS)
# ==========================================================================

pygame.quit()
