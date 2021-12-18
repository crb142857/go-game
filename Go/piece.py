import pygame as pg
from pygame.sprite import Sprite


class WhitePieceUp(Sprite):
    def __init__(self, go_setting, screen, spot=None):
        super(WhitePieceUp, self).__init__()
        self.go_setting = go_setting
        self.screen = screen
        self.image = pg.image.load(self.go_setting.piece_white_name_up).convert_alpha()
        self.cursor_x, self.cursor_y = 0
        self.piece_kind = 1
        self.rect = self.image.get_rect()
        self.mouse_control = True
        self.spot = spot

    def blit_piece(self):
        if self.mouse_control:
            self.cursor_x, self.cursor_y = pg.mouse.get_pos()
        if not self.mouse_control:
            self.cursor_x, self.cursor_y = self.spot.centerx, self.spot.centery
        self.cursor_x -= self.image.get_width()/2
        self.cursor_y -= self.image.get_height()/2
        self.screen.blit(self.image, (self.cursor_x, self.cursor_y))


class BlackPieceUp(Sprite):
    def __init__(self, go_setting, screen, spot=None):
        super(BlackPieceUp, self).__init__()
        self.go_setting = go_setting
        self.screen = screen
        self.image = pg.image.load(self.go_setting.piece_black_up_name).convert_alpha()
        self.cursor_x, self.cursor_y = 0
        self.piece_kind = 0
        self.rect = self.image.get_rect()
        self.mouse_control = True
        self.spot = spot

    def blit_piece(self):
        if self.mouse_control:
            self.cursor_x, self.cursor_y = pg.mouse.get_pos()
        if not self.mouse_control:
            self.cursor_x, self.cursor_y = self.spot.centerx, self.spot.centery
        self.cursor_x -= self.image.get_width()/2
        self.cursor_y -= self.image.get_height()/2
        self.screen.blit(self.image, (self.cursor_x, self.cursor_y))
