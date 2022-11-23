import random


def convert_char_into_bin(char: str) -> str:
    return format(ord(char[0]), "08b")

def replace_text_with_space(text: str) -> str:
    normal_space: str = "\u0020"
    nobreak_space: str = "\u00A0"
    text_bin: str = "".join(list(map(
        lambda char: convert_char_into_bin(char),
        text
    )))
    return "".join(list(map(
        lambda binary: normal_space if binary == "0" else nobreak_space,
        text_bin
    )))

def hide_text(text: str, cover_words: list[str]) -> str:
    space_text: str = replace_text_with_space(text)
    return "".join(list(map(
        lambda space: random.choice(cover_words) + space,
        space_text
    ))) + random.choice(cover_words)


if __name__ == "__main__":
    pass

