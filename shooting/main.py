# -*- coding: utf-8 -*-
import pygame

pygame.init() # pygameの初期化しないとエラーになる

# ウインドウの作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# FPSの設定
FPS = 60
clock = pygame.time.Clock()

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# メインループ =============================================================
run = True
while run:
    # 背景の描画
    screen.fill(BLACK)

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
