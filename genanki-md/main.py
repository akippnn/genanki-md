import argparse
import itertools
import random
import json

from typing import LiteralString, TextIO

from .core import create_notes, create_package
from .errors import InvalidSyntax
from .parsers import parse_input
from .builtin_models import MODELS, Model

DESCRIPTION: str = "Generate an Anki deck from a Markdown file"
DEFAULT_MODEL: str = "b" # see builtin_models.py
DATA_FILE: TextIO = lambda mode: open("data.json", mode=mode)
REGEXP: LiteralString = r"> \[(!anki)(?:-([\w-]+))?\]"

try:
    fp = DATA_FILE("r")
    DATA = json.load(fp)

except FileNotFoundError:
    fp = DATA_FILE("w")
    DATA = {}
    json.dump(DATA, fp)

finally:
    fp.close()


def get_front_text(line: str) -> str:
    line = line[line.find("]") + 1:]
    if line[0] in ["-", "+"]:
        line = line[1:]
    elif not line[0] == " ":
        raise InvalidSyntax(f"Invalid syntax for foldable callouts in \"{line}\".")
    return line.strip()


def get_back_text(file_iter: TextIO) -> str:
    line = file_iter.readline()
    if line.startswith(">"):
        current_back = ""
        while line.startswith(">"):
            current_back += line[1:].strip() + "<br>"
            line = file_iter.readline()
        return current_back
    else:
        return line.strip()


def main() -> None:
    argp = argparse.ArgumentParser(description=DESCRIPTION)
    argp.add_argument("--source", "-s",
                      type=argparse.FileType("r", encoding="utf-8"),
                      required=True,
                      action="append",
                      help="Path to the input UTF-8 file to be parsed")
    argp.add_argument("--output", "-o",
                      required=True,
                      help="Anki deck package to be generated")
    argp.add_argument("--verbose", "-v",
                      action="store_true")
    argp.add_argument("--model", "-m",
                      default=DEFAULT_MODEL,
                      choices=MODELS.keys(),
                      help="Model used when the option was not specified for that individual callout (see genanki-md/models.py)")
    argp.add_argument("--css",
                      type=argparse.FileType("r"),
                      help="Override the default CSS of all the models with your own CSS file (see example.css)")
    args = argp.parse_args()
  
    input_files: list = args.source
    output_file: str = args.output
    verbose: bool = args.verbose
    model: Model = MODELS[args.model]
    css: str | None = args.css.readline() if args.css else None

    try:
        DATA[output_file]
        deck_uid = DATA[output_file]["deck_uid"]
    except:
        deck_uid = random.randrange(1 << 30, 1 << 31)
        DATA[output_file] = { "deck_uid": deck_uid }
        with DATA_FILE("w") as fp:
            json.dump(DATA, fp)

    if verbose:
        verbose = lambda x: print(x)
    else:
        verbose = lambda x: ...

    parsed_files = list()
    notes = iter(())

    for file in input_files:
        parsed_files.append(parse_input(
            infile=file,
            models=MODELS,
            regexp=REGEXP,
            _front_text=get_front_text,
            _back_text=get_back_text))

    for file in parsed_files:
        notes = itertools.chain(notes, create_notes(
            file=file,
            models=MODELS,
            model=model,
            css = css,
            _callback = verbose
        ))

    package = create_package(
        unique_id=deck_uid,
        name=output_file,
        notes=notes)

    package.write_to_file(f"{output_file}.apkg")

if __name__ == "__main__":
    main()