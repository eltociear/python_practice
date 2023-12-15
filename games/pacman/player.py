import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    """
    プレイヤークラス
    """
    change_x = 0
    change_y = 0
    explosion = False
    game_over = False

    def __init__(self, x, y, filename):
        """
        初期化関数
        """
        # 親クラスのコンストラクタを呼ぶ
        pygame.sprite.Sprite.__init__(self)
        # 画像を読み込む
        self.image = pygame.image.load(filename).convert()
        # 色を設定し、透明色を設定
        self.image.set_colorkey(BLACK)
        # 位置を設定
        self.rect = self.image.get_rect()
        # 画像の左上すみの座標を設定
        self.rect.topleft = (x, y)

        img = pygame.image.load(PLAYER_IMAGE).convert()

        # 右移動のアニメーション
        self.move_right_animation = Animation(img, 32, 32)
        # 左移動のアニメーション（右移動の画像を反転）
        self.move_left_animation = Animation(pygame.transform.flip(img, True, False), 32, 32)
        # 上移動のアニメーション（90度回転）
        self.move_up_animation = Animation(pygame.transform.rotate(img, 90), 32, 32)
        # 下移動のアニメーション（270度回転）
        self.move_down_animation = Animation(pygame.transform.rotate(img, 270), 32, 32)

        # 爆発時のアニメーション
        self.explosion_animation = Animation(img, 32, 32)

        # プレイヤーの画像を読み込む
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)

    def update(self, horizontal_blocks, vertical_blocks):
        """
        更新関数
        """
        # 爆発していない場合
        if not self.explosion:
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
            # プレイヤーを移動
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            # プレイヤーと水平方向のブロックとの衝突判定
            for block in pygame.sprite.spritecollide(self, horizontal_blocks, False):
                self.rect.centery = block.rect.centery
                # ブロックがあるので移動しない
                self.change_y = 0
            # プレイヤーと垂直方向のブロックとの衝突判定
            for block in pygame.sprite.spritecollide(self, vertical_blocks, False):
                self.rect.centerx = block.rect.centerx
                # ブロックがあるので移動しない
                self.change_x = 0

            # x方向の移動が正
            if self.change_x > 0:
                # 右移動のアニメーションを表示
                self.move_right_animation.update(10)
                self.image = self.move_right_animation.get_current_image()
            # x方向の移動が負
            elif self.change_x < 0:
                # 左移動のアニメーションを表示
                self.move_left_animation.update(10)
                self.image = self.move_left_animation.get_current_image()

            # y方向の移動が正
            if self.change_y > 0:
                # 下移動のアニメーションを表示
                self.move_down_animation.update(10)
                self.image = self.move_down_animation.get_current_image()
            # y方向の移動が負
            elif self.change_y < 0:
                # 上移動のアニメーションを表示
                self.move_up_animation.update(10)
                self.image = self.move_up_animation.get_current_image()
        # 爆発している場合
        else:
            if self.explosion_animation.index == self.explosion_animation.get_length() - 1:
                # 少し時間をおいてゲームオーバー
                pygame.time.wait(500)
                self.game_over = True
            self.explosion_animation.update(12)
            # 爆発時の画像を設定
            self.image = self.explosion_animation.get_image()

    def move_right(self):
        """
        右に移動
        """
        self.change_x = 3

    def move_left(self):
        """
        左に移動
        """
        self.change_x = -3

    def move_up(self):
        """
        上に移動
        """
        self.change_y = -3

    def move_down(self):
        """
        下に移動
        """
        self.change_y = 3

    def stop_move_right(self):
        """
        右移動を停止したら、デフォルトのプレイヤー画像を表示
        """
        if self.change_x != 0:
            self.image = self.player_image
        self.change_x = 0

    def stop_move_left(self):
        """
        左移動を停止したら、デフォルトのプレイヤー画像を表示
        """
        if self.change_x != 0:
            self.image = pygame.transform.flip(self.player_image, True, False)
        self.change_x = 0

    def stop_move_up(self):
        """
        上移動を停止したら、デフォルトのプレイヤー画像を表示
        """
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image, 90)
        self.change_y = 0

    def stop_move_down(self):
        """
        下移動を停止したら、デフォルトのプレイヤー画像を表示
        """
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image, 270)
        self.change_y = 0

class Animation(object):
    """
    アニメーションクラス
    """
    def __init__(self, img, width, height):
        """
        初期化関数
        """
        self.sprite_sheet = img
        self.image_list = []
        self.load_images(width, height)
        self.index = 0
        self.clock = 1

    def load_images(self, width, height):
        """
        スプライトシートに並んだ画像をそれぞれリストに入れる
        """
        for y in range(0, self.sprite_sheet.get_height(), height):
            for x in range(0, self.sprite_sheet.get_width(), width):
                img = self.get_image(x, y, width, height)
                self.image_list.append(img)

    def get_image(self, x, y, width, height):
        """
        スプライトシートから画像を切り出す
        """
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image

    def get_current_image(self):
        """
        現在の画像を取得
        """
        return self.image_list[self.index]

    def get_length(self):
        """
        画像の枚数を取得
        """
        return len(self.image_list)

    def update(self, fps=30):
        """
        画像を更新する
        frame per second（fps）が30の場合はstep数は1
        """
        step = 30 // fps
        if self.clock == 30:
            self.clock = 1
        else:
            self.clock += 1

        if self.clock in range(1, 30, step):
            self.index += 1
            if self.index == len(self.image_list):
                self.index = 0
