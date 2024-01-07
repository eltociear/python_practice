import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GLID_WIDTH = WIDTH // TILE_SIZE
GLID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GLID_HEIGHT), random.randrange(0, GLID_WIDTH)) for _ in range(num)])

def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GLID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)) # 横線

    for col in range(GLID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT)) # 縦線

def main():
    running = True
    playing = False

    positions = set()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() # クリックした位置を取得
                col = x // TILE_SIZE # クリックした位置をグリッドの位置に変換
                row = y // TILE_SIZE # クリックした位置をグリッドの位置に変換
                pos = (col, row) # グリッドの位置をタプルにまとめる

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions.set()
                    playing = False

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4, 10) * GLID_WIDTH) # Gを押すとグリッドがランダムに生成される

        screen.fill(GRAY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
