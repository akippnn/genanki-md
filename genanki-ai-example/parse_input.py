import sys

def parse_input(input_file):
    cards = []
    current_front = ""
    current_back = ""

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line.startswith("Front: "):
                    if current_front:
                        cards.append((current_front, current_back))
                    current_front = line[len("Front: "):]
                    current_back = ""
                elif line.startswith("Back: "):
                    current_back = line[len("Back: "):]
                else:
                    current_back += line + "<br>"

            if current_front:
                cards.append((current_front, current_back))
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

    return cards
