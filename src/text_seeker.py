def split_text(text: str, digits: int) -> list[str]:
    return [text[idx:idx + digits] for idx in range(0, len(text), digits)]

def convert_bin_into_char(binary: str) -> str:
    return chr(int(binary[0:8], 2))

def replace_space_with_text(space: str) -> str:
    japanese_space: str = "　"
    space_bin: str = "".join(list(map(
        lambda s_bin: "1" if s_bin == japanese_space else "0",
        space
    )))
    divided_space_bin: list[str] = split_text(space_bin, 8)
    return "".join(list(map(
        lambda s_bin: convert_bin_into_char(s_bin), divided_space_bin
    )))

def find_hidden_text(cover_text: str) -> str:
    normal_space: str = " "
    japanese_space: str = "　"
    space_text: str = "".join(list(map(
        lambda char: char if char in [normal_space, japanese_space] else "",
        cover_text
    )))
    return replace_space_with_text(space_text)


if __name__ == "__main__":
    pass

