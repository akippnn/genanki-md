import re
import sys

from typing import Callable, LiteralString, TextIO
from genanki.model import Model

from .errors import InvalidCommand


class Card:
    def __init__(
            self, 
            front: str, 
            back: str,
            model: str | None):

        self.front = front
        self.back = back
        self.model = model


def parse_input(
        infile: TextIO,
        models: dict[str, Model],
        regexp: LiteralString,
        _front_text_callback: Callable[[str], str],
        _back_text_callback: Callable[[TextIO], str]
        ) -> set[Card]:

    cards = set() 
    command_pattern = re.compile(regexp)

    try:
        for line in infile:
            match = command_pattern.match(line)
            if not match:
                continue

            command, option = match.groups()

            if option in models:
                current_model = option 
            elif option:
                raise InvalidCommand(f"\"{option}\" is not a subcommand.")
            else:
                current_model = None

            current_front = _front_text_callback(line)
            current_back = _back_text_callback(infile)

            cards.add(Card(
                current_front,
                current_back,
                current_model))

    except StopIteration:
        pass

    except FileNotFoundError:
        print(f"File '{infile}' not found.")
        sys.exit(1)

    finally:
        infile.close()

    return cards
