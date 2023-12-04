import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # 背景
        self.bg_img = pygame.image.load("shooting/assets/img/background/bg.png")

    def run(self):
        self.screen.blit(self.bg_img, (0, 0))
