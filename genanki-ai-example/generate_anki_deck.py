import genanki
from parse_input import parse_input

def generate_anki_deck(deck_name, parsed_cards):
    deck = genanki.Deck(1, deck_name)

    for front, back in parsed_cards:
        note = genanki.Note(
            model=genanki.Model(
                2,
                "Simple Model",
                fields=[
                    {"name": "Front"},
                    {"name": "Back"},
                ],
                templates=[
                    {
                        "name": "Card 1",
                        "qfmt": '{{Front}}',
                        "afmt": '{{Front}}<br>{{Back}}',
                    },
                ],
            ),
            fields=[front, back],
        )

        deck.add_note(note)

    return deck
