import pygame as pg
from spot import Spot
from piece import WhitePieceUp
from piece import BlackPieceUp


def check_collision_event(spots, mouse_pieces, event):
    if event.type == pg.MOUSEBUTTONUP:
        mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()
        pos_next = pg.sprite.groupcollide(mouse_pieces, spots, False, False)
        for spot in spots:
            if int(mouse_pos_x) + 20 >= spot.centerx >= int(mouse_pos_x) - 20:
                if int(mouse_pos_y) + 20 >= spot.centery >= int(mouse_pos_y) - 20:
                    for mouse_piece in mouse_pieces:
                        mouse_piece.mouse_control = False


def update_screen(go_setting, screen, spots, mouse_pieces):
    screen.fill(go_setting.bg_color)
    board = pg.image.load(go_setting.board_name).convert_alpha()
    screen.blit(board, (0, 0))
    for spot in spots:
        spot.blit_spot()
    draw_piece_mouse(mouse_pieces, go_setting, screen)
    for mouse_piece in mouse_pieces:
        mouse_piece.blit_piece()
    pg.display.flip()
    pg.display.update()


def music(go_setting):
    pg.mixer.music.load(go_setting.music_name)
    pg.mixer.music.play(-1, 0.0)
    pg.mixer.music.set_volume(1.0)


def draw_spots(go_setting, screen, spots):
    spot_num_x = 0
    spot_num_y = 0
    while spot_num_x <= 18:
        spot = Spot(go_setting, spot_num_x, spot_num_y, screen)
        spots.add(spot)
        while spot_num_y <= 18:
            spot_num_y += 1
            spot = Spot(go_setting, spot_num_x, spot_num_y, screen)
            spots.add(spot)
        spot_num_x += 1
        spot_num_y = 0


def draw_piece_mouse(mouse_pieces, go_setting, screen):
    if len(mouse_pieces) == 0:
        if go_setting.control_first:
            black_piece = BlackPieceUp(go_setting, screen)
            mouse_pieces.add(black_piece)
        if not go_setting.control_first:
            white_piece = WhitePieceUp(go_setting, screen)
            mouse_pieces.add(white_piece)
