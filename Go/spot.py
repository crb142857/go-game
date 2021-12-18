import pygame as pg
from pygame.sprite import Sprite


class Spot(Sprite):
    def __init__(self, go_setting, num_x, num_y, screen):
        super(Spot, self).__init__()
        self.image = pg.image.load(go_setting.spot_name)
        self.rect = self.image.get_rect()
        self.rect.centerx = 20 + go_setting.spot_space_leftright * num_x
        self.rect.centery = 16 + go_setting.spot_space_updown * num_y
        self.screen = screen

    def blit_spot(self):
        self.screen.blit(self.image, self.rect)

