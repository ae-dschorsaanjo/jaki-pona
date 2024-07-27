from PIL import Image, ImageDraw
from copy import deepcopy

ORIGINAL = "pics/sitelen_pona_leko/sitelen-pona-leko-trans.png"
OUT_DIR = "docs/pics/"
BORDER_WIDTH = 4
IMAGE_WIDTH = 148
IMAGE_HEIGHT = 120
TEXT_HEIGHT = 24
ROWS = 14
COLUMNS = 10
WORDS = [
    "a",
    "akesi",
    "ala",
    "alasa",
    "ale",
    "anpa",
    "ante",
    "anu",
    "apeja",
    "awen",
    "e",
    "en",
    "esun",
    "ijo",
    "ike",
    "ilo",
    "insa",
    "jaki",
    "jan",
    "jelo",
    "jo",
    "kala",
    "kalama",
    "kama",
    "kasi",
    "ken",
    "kepeken",
    "kijetesantakalu",
    "kili",
    "kin",
    "kipisi",
    "kiwen",
    "ko",
    "kon",
    "ku",
    "kule",
    "kulupu",
    "kute",
    "la",
    "lanpan",
    "lape",
    "laso",
    "lawa",
    "leko",
    "len",
    "lete",
    "li",
    "lili",
    "linja",
    "lipu",
    "loje",
    "lon",
    "luka",
    "lukin",
    "lupa",
    "ma",
    "majuna",
    "mama",
    "mani",
    "meli",
    "mi",
    "mije",
    "moku",
    "moli",
    "monsi",
    "monsuta",
    "mu",
    "mun",
    "musi",
    "mute",
    "namako",
    "nanpa",
    "nasa",
    "nasin",
    "nena",
    "ni",
    "nimi",
    "noka",
    "o",
    "oko",
    "olin",
    "ona",
    "open",
    "pakala",
    "pake",
    "pali",
    "palisa",
    "pan",
    "pana",
    "pi",
    "pilin",
    "pimeja",
    "pini",
    "pipi",
    "poka",
    "poki",
    "pona",
    "powe",
    "pu",
    "sama",
    "seli",
    "selo",
    "seme",
    "sewi",
    "sijelo",
    "sike",
    "sin",
    "sina",
    "sinpin",
    "sitelen",
    "sona",
    "soweli",
    "su",
    "suli",
    "suno",
    "supa",
    "suwi",
    "tan",
    "taso",
    "tawa",
    "telo",
    "tenpo",
    "toki",
    "tomo",
    "tonsi",
    "tu",
    "unpa",
    "uta",
    "utala",
    "walo",
    "wan",
    "waso",
    "wawa",
    "weka",
    "wile",
    "yupekosi",
]


def read_image(path):
    return Image.open(path)


def tile_coordinate(x, y):
    return (
        x * BORDER_WIDTH + (x - 1) * IMAGE_WIDTH,
        y * BORDER_WIDTH + (y - 1) * IMAGE_HEIGHT + (y - 1) * TEXT_HEIGHT,
        x * BORDER_WIDTH + x * IMAGE_WIDTH,
        y * BORDER_WIDTH + y * IMAGE_HEIGHT + (y - 1) * TEXT_HEIGHT,
    )


def draw(img, x, y):
    i = deepcopy(img)
    imgdraw = ImageDraw.Draw(i)
    imgdraw.rectangle(
        xy=tile_coordinate(x, y),
        fill=(255, 0, 0),
    )
    #   outline = (255, 0, 0),
    #   width = 0)
    return i


def crop(img, x, y):
    i = deepcopy(img)
    return i.crop(tile_coordinate(x, y))


def coordinate_test():
    original = read_image(ORIGINAL)
    i = draw(original, 1, 1)
    control = 1
    for y in range(1, ROWS + 1):
        for x in range(1, COLUMNS + 1):
            try:
                name = WORDS[(y - 1) * 10 + x - 1]
                print(name, f"({control})")
                control += 1
                i = draw(i, x, y)
                print(x, y)
                print("")
                i.save(OUT_DIR + f"{name}.png")
            except:
                print("done!")
                return


def main():
    original = read_image(ORIGINAL)
    control = 1
    for y in range(1, ROWS + 1):
        for x in range(1, COLUMNS + 1):
            try:
                name = WORDS[(y - 1) * 10 + x - 1]
                print(name, f"({control})")
                control += 1
                i = crop(original, x, y)
                print(x, y)
                print("")
                i.save(OUT_DIR + f"{name}.png")
            except:
                print("done!")
                return


if __name__ == "__main__":
    # coordinate_test()
    main()
