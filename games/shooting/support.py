import pygame

def draw_text(screen, txt, x, y, size, color):
    font = pygame.font.Font(None, size)
    surface = font.render(txt, True, color) # txt: 表示する文字列, True: アンチエイリアス, color: 文字色
    x = x - surface.get_width() / 2 # 左上側が基準点になるため、中心が基準になるように調整
    y = y - surface.get_height() / 2 # xと同様に調整
    screen.blit(surface, (x, y))
