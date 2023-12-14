import pygame
from game import Game

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    """
    main関数
    """

    # Pygameの初期化 (必須)
    pygame.init()

    # 画面の大きさを設定して画面を生成
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # タイトルバーの文字列を設定
    pygame.display.set_caption("PACMAN")

    # ゲーム実行フラグ
    done = False
    # 時計オブジェクトを生成
    clock = pygame.time.Clock()
    # ゲームオブジェクトを生成
    game = Game()

    # ゲームループ
    while not done:
        # Gameクラスのprocess_events関数を実行。戻り値をdoneに代入
        done = game.process_events()
        # Gameクラスのrun_logic関数を実行
        game.run_logic()
        # Gameクラスのdisplay_frame関数を実行
        game.display_frame(screen)
        # フレームレートを設定
        clock.tick(30)
    # 実行フラグがFalseになったらPygameを終了
    pygame.quit()

if __name__ == "__main__":
    main()
