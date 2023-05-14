def __init__(self, width, height, offset_vertical, offset_horizontal):
    self.width = width
    self.height = height
    self.offset_vertical = offset_vertical
    self.offset_horizontal = offset_horizontal
    self.tile_size = (min(self.height, self.width) - 2 * max(self.offset_vertical, self.offset_horizontal)) / 8

def get_square_cords_from_cords(self, pos):
    x, y = self.pixel_to_cords(pos)
    index = self.cords_to_index(x, y)
    x, y = self.index_to_pixel(index)
    return x, y
def index_to_cords(self, index):
    x = index % 8
    y = 7 - int(index / 8)
    return x, y

def index_to_pixel(self, index):
    x = self.offset_vertical + (index % 8) * self.tile_size
    y = self.height - (int(index / 8) + 1) * self.tile_size

    return x, y
def cords_to_index(self, x, y):
    index = 56 - y * 8 + (x % 8)
    return index

def pixel_to_cords(self, pos):
    x = int((pos[0] - self.offset_vertical)/self.tile_size % 8)
    y = int((pos[1] - self.offset_vertical)/self.tile_size)
    return x, y

def cords_inside_board(self, pos):
    return self.offset_horizontal <= pos[0] <= self.width - self.offset_horizontal and \
        self.offset_vertical <= pos[1] <= self.height - self.offset_vertical
