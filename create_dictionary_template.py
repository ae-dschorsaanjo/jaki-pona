#! /usr/bin/env python3

from pyperclip import copy
from re import match, sub


def pos_maker(*list: list[str, str, str]) -> list[dict[str, str]]:
    out = []
    for line in list:
        out.append({"en": line[0], "hu": line[1], "huname": line[2]})
    return out


POS = pos_maker(
    ["n", "f", "főnév"],
    ["v", "i", "ige"],
    ["a", "s", "segédige"],
    ["p", "e", "előljáró"],
    ["m", "m", "módosítószó"],
    ["f", "n", "nyelvtani szó"],
    ["#", "#", "szám"],
    ["i", "!", "indulatszó, felkiáltás"],
    ["c", "k", "kötőszó"],
    ["l", "l", "*la* előtti jelentés"],
    ["pu", "pu", "pu-beli verzió"],
    ["see", "ld", "lásd"],
)

POS_EN = {x["en"]: [x["hu"], x["huname"]] for x in POS}

REGEX_WORD = r"__(\\\*)?[\w/ ,]+__"
REGEX_MEANING = r"`([^`]+)`&shy;`([^`]+)`\s*(.*)"


def read_file(file: str) -> list[str]:
    with open(file, "r", encoding="utf-8") as f:
        return f.readlines()


def replace_pos(match) -> str:
    parts = []
    if (m := match[1]) in POS_EN:
        m = POS_EN[m][0]
    return f"`{m}`&shy;`{match[2]}` {match[3]}  "


def replace_meaning(line: str) -> str:
    if match(REGEX_MEANING, line):
        line = sub(REGEX_MEANING, replace_pos, line)
    return line


def parse_file(file: str) -> list[dict[str, str]]:
    out = []
    is_intro = True
    for line in read_file(file):
        line = line.strip()

        if is_intro:
            if line == "### A":
                is_intro = False
                out.append(line)
            else:
                continue

        out.append(replace_meaning(line))
    return out


def create_template():
    hun_template = "\n".join(parse_file("dict_en.md"))
    copy(hun_template)


def create_pos():
    s = ""
    for line in POS:
        s += f"`{line['hu']}`\n`: {line['huname']}\n\n"
    copy(s)


def main():
    # create_template()
    create_pos()


if __name__ == "__main__":
    main()
