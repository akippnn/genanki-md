import argparse
import parse_input, generate_anki_deck

def main():
    parser = argparse.ArgumentParser(description="Generate Anki decks from input text.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("deck_name", help="Name of the Anki deck")

    args = parser.parse_args()
    
    input_file = args.input_file
    deck_name = args.deck_name

    parsed_cards = parse_input.parse_input(input_file)
    deck = generate_anki_deck.generate_anki_deck(deck_name, parsed_cards)

    # Continue using the 'deck' object or perform other actions as needed.

if __name__ == "__main__":
    main()
