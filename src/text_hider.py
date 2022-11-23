import random


def convert_char_into_bin(char: str) -> str:
    return format(ord(char[0]), "08b")

def replace_text_with_space(text: str) -> str:
    normal_space: str = " "
    japanese_space: str = "　"
    text_bin: str = "".join(list(map(
        lambda char: convert_char_into_bin(char),
        text
    )))
    return "".join(list(map(
        lambda binary: normal_space if binary == "0" else japanese_space,
        text_bin
    )))

def hide_text(text: str, random_text: list[str]) -> str:
    space_text: str = replace_text_with_space(text)
    return "".join(list(map(
        lambda space: random.choice(random_text) + space,
        space_text
    ))) + random.choice(random_text)


if __name__ == "__main__":
    pass

