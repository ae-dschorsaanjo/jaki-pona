from PIL import Image, ImageDraw
from copy import deepcopy

ORIGINAL = "res/sitelen_pona_leko/sitelen-pona-leko-trans.png"
OUT_DIR = "docs/pics/"
BORDER_WIDTH = 4
IMAGE_WIDTH = 148
IMAGE_HEIGHT = 120
TEXT_HEIGHT = 24
ROWS = 14
COLUMNS = 10


def read_image(path):
    return Image.open(path)


def tile_coordinate(x, y):
    return (x * BORDER_WIDTH + (x-1) * IMAGE_WIDTH,
            y * BORDER_WIDTH + (y-1) * IMAGE_HEIGHT + (y-1) * TEXT_HEIGHT,
            x * BORDER_WIDTH + x * IMAGE_WIDTH,
            y * BORDER_WIDTH + y * IMAGE_HEIGHT + (y-1) * TEXT_HEIGHT)


def draw(img, x, y):
    i = deepcopy(img)
    imgdraw = ImageDraw.Draw(i)
    print(tile_coordinate(x, y))
    imgdraw.rectangle(xy = tile_coordinate(x, y),
                      fill = (255, 0, 0),)
                    #   outline = (255, 0, 0),
                    #   width = 0)
    return i


def crop_to_tile(img, x, y):
    ...


def coordinate_test():
    original = read_image(ORIGINAL)
    i = draw(original, 1, 1)
    i = draw(i, 2, 1)
    i = draw(i, 3, 2)
    i = draw(i, 5, 5)
    i.save(OUT_DIR + "test.png")


if __name__ == '__main__':
    pass
