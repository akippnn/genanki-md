from genanki.builtin_models import BASIC_MODEL
from genanki.builtin_models import BASIC_AND_REVERSED_CARD_MODEL
from genanki.builtin_models import BASIC_OPTIONAL_REVERSED_CARD_MODEL
from genanki.builtin_models import BASIC_TYPE_IN_THE_ANSWER_MODEL
from genanki.builtin_models import CLOZE_MODEL

from genanki.model import Model

MODELS: dict[str, Model] = {
  "b": BASIC_MODEL,
  "r": BASIC_AND_REVERSED_CARD_MODEL,
  "o": BASIC_OPTIONAL_REVERSED_CARD_MODEL,
  "t": BASIC_TYPE_IN_THE_ANSWER_MODEL,
  "c": CLOZE_MODEL
}