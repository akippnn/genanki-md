import genanki
import sys

from collections.abc import Callable, Iterator
from .builtin_models import MODELS
from .parsers import Card


def create_notes(
        cards: list[Card],
        default_model: genanki.Model,
        css: str | None = None,
        _callback: Callable[[genanki.Note], any] = None
        ) -> Iterator[genanki.Note]:

    for card in cards:
        if not card.model:
            model = MODELS[default_model]
        else:
            model = MODELS[card.model]
        
        if css:
            model.css = css

        note = genanki.Note(
            model=model,
            fields=[card.front, card.back])

        _callback(note) if _callback else ...
        yield note


def create_package(
        unique_id: int, 
        name: str, 
        notes: Iterator[genanki.Note]):

    deck = genanki.Deck(
        unique_id,
        name)

    for note in notes:
        deck.add_note(note)

    return genanki.Package(deck)
