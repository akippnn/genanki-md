# genanki-md

genanki-md is a Python wrapper for genanki that facilitates parsing UTF-8 files using the [Obsidian-Flavored](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown) Markdown Callouts syntax.

## Roadmap

- [ ] Add GUI

## Usage

To use genanki-md, create a markdown file in the Obsidian app, utilizing the Callouts syntax. For instance:

```md
> [!anki-b] Question  
> Answer

> [!anki-r] Basic and Reversed
Two cards!

> [!anki-c] Cloze model
> {{c1:Rome}} is the capital city of Italy.
```

For more details, see the examples in the "File" section below.

## Requirements

- `poetry`

If you are using [Nix](https://en.wikipedia.org/wiki/Nix_(package_manager)), you can run `nix shell` in your local copy of this repository to set up the environment.

## Installation

Install the necessary dependencies and cache using the following:

```sh
poetry install --no-root
```

To verify that everything is set up correctly:

```sh
$ poetry run ga
usage: ga.cmd [-h] --source SOURCE, --output OUTPUT, [--verbose] [--model {b,r,o,t,c}] [--css CSS]
ga.cmd: error: the following arguments are required: --source/-s, --output/-s
```

## File

To begin, create a markdown file using the Obsidian app. For example, a card with a basic model and a one-line answer may look like this:

```md
> [!anki-b] Question  
Answer
```

Obsidian's support for any keyword inside the Callouts syntax allows for versatile use regardless of supported type.

```md
> [!anki-b]- What does this do?
> Foldable callouts!  
> Another line.
```

Currently, you will have to use the Terminal to create notes. For example:

```sh
poetry run ga -s {file1} -s {file2} -v -m {model} -o {output}
```

## Models

genanki-md supports the following models:

```py
MODELS: dict[str, Model] = {
  "b": BASIC_MODEL,
  "r": BASIC_AND_REVERSED_CARD_MODEL,
  "o": BASIC_OPTIONAL_REVERSED_CARD_MODEL,
  "t": BASIC_TYPE_IN_THE_ANSWER_MODEL,
  "c": CLOZE_MODEL
}
```

Choose the appropriate model based on your desired card type.
