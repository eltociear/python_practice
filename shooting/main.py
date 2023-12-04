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
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
# ==========================================================================

pygame.quit()
