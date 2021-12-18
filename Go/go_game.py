import sys
import pygame as pg
from pygame.sprite import Group
import go_settings
import functions
import time

# 编写时间：2021年8月15日16:56:31
# 最后修改：2021年12月13日09:27:23


def go_game():
    pg.init()
    pg.mouse.set_visible(True)
    go_setting = go_settings.Set()
    screen = pg.display.set_mode((go_setting.screen_width, go_setting.screen_highth))
    spots = Group()
    mouse_pieces = Group()
    black_piece = Group()
    white_piece = Group()
    pg.display.set_caption("围棋")
    functions.music(go_setting)
    functions.draw_spots(go_setting, screen, spots)
    while True:
        functions.update_screen(go_setting, screen, spots, mouse_pieces)
        time.sleep(0.003)
        for event in pg.event.get():
            functions.check_collision_event(spots, mouse_pieces, event)
            if event.type == pg.QUIT:
                sys.exit()


if __name__ == "__main__":
    go_game()
