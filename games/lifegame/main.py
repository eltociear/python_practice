import pygame

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

def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GLID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GLID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def main():
    running = True

    positions = set()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

        screen.fill(GRAY)
        draw_grid(positions)
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
