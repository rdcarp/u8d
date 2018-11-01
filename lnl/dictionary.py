from pathlib import Path

WORDS_FILE = Path(__file__) / "../resources/words.txt"


def load_words():
    with open(WORDS_FILE) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
