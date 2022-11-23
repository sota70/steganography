import sys
import getopt
import text_hider
import text_seeker


def write_text_to_file(file_path: str, text: str) -> bool:
    try:
        with open(file_path, "w") as file:
            file.write(text)
        return True
    except:
        return False

def read_text_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return "".join(file.readlines())

def hide_text(options: dict[str, str], option_name: dict[str, str]) -> bool:
    cover_words: list[str]
    cover_file_path: str
    secret_file_path: str
    output_file_path: str
    secret_text: str
    if len(options) < 3:
        print("Not enough arguments to run the command")
        return False
    output_file_path = options[option_name["output"]]
    secret_file_path = options[option_name["secret"]]
    cover_file_path = options[option_name["cover"]]
    with open(cover_file_path, "r") as file:
        cover_words = list(map(
            lambda text: text.replace("\n", ""),
            file.readlines()
        ))
    secret_text = read_text_from_file(secret_file_path)
    secret_text = text_hider.hide_text(secret_text, cover_words)
    return True if write_text_to_file(output_file_path, secret_text) else False

def seek_text(options: dict[str, str], option_name: dict[str, str]) -> bool:
    output_file_path: str
    hidden_text_path: str
    hidden_text: str
    discovered_text: str
    if len(options) < 2:
        print("Not enough arguments to run the command")
        return False
    hidden_text_path = options[option_name["secret"]]
    output_file_path = options[option_name["output"]]
    hidden_text = read_text_from_file(hidden_text_path)
    discovered_text = text_seeker.find_hidden_text(hidden_text)
    write_text_to_file(output_file_path, discovered_text)
    return True

def run_command(command: str, options: dict[str, str], commands: dict, option_name: dict[str, str]) -> bool:
    if not command in commands:
        print("Unknown command")
        return False
    return commands[command](options, option_name)

def convert_tuples_into_dict(tuples: list[tuple]) -> dict:
    dictionary: dict = {}
    for key, value in tuples:
        dictionary[key] = value
    return dictionary


def main() -> int:
    # 第１引数はこのスクリプト自身を指定するから要らない
    # そして第２引数もコマンド名を指定するからコマンド引数には入らない
    command: str = sys.argv[1]
    arguments: list[str] = sys.argv[2:]
    options: list[tuple[str, str]]
    commands: dict = {
        "hide": hide_text,
        "seek": seek_text
    }
    command_option_name: dict[str, str] = {
        "secret": "-s",
        "output": "-o",
        "cover": "-c"
    }
    options, arguments = getopt.getopt(
        arguments,
        # option:option2:option3の形にしないとコマンドオプションを取得できない
        "".join(list(map(
            lambda option: option.replace("-", "") + ":",
            command_option_name.values()
        )))
    )
    return 0 if run_command(command, convert_tuples_into_dict(options), commands, command_option_name) else 1


if __name__ == "__main__":
    print("Script executed successfully" if main() == 0 else "Something went wrong")

