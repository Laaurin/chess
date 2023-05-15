from config import *


def get_square_cords_from_cords(pos):
    x, y = pixel_to_cords(pos)
    index = cords_to_index(x, y)
    x, y = index_to_pixel(index)
    return x, y


def index_to_cords(index):
    x = index % 8
    y = 7 - int(index / 8)
    return x, y


def index_to_pixel(index):
    x = OFFSET_VERTICAL + (index % 8) * TILE_SIZE
    y = WINDOW_HEIGHT - (int(index / 8) + 1) * TILE_SIZE

    return x, y


def cords_to_index(x, y):
    index = 56 - y * 8 + (x % 8)
    return index


def pixel_to_cords(pos):
    x = int((pos[0] - OFFSET_VERTICAL) / TILE_SIZE % 8)
    y = int((pos[1] - OFFSET_VERTICAL) / TILE_SIZE)
    return x, y


def cords_inside_board(pos):
    return OFFSET_HORIZONTAL <= pos[0] <= WINDOW_WIDTH - OFFSET_HORIZONTAL and \
        OFFSET_VERTICAL <= pos[1] <= WINDOW_HEIGHT - OFFSET_VERTICAL
