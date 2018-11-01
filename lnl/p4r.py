import random
import re


class P4r:
    def __init__(self, word_list):
        self.word_list = word_list

    def _make_regex(self, _in):
        start = _in[0]
        middle = _in[1:-1]
        end = _in[-1]

        return re.compile(r"^{}.{{{}}}{}$".format(start, middle, end))

    def _get_expansions(self, short):
        reg = self._make_regex(short)

        matches = []
        for w in self.word_list:
            if reg.match(w):
                matches.append(w)

        return matches

    def longify_random(self, short):
        words = self._get_expansions(short)
        return random.choice(words)

    def longify_list(self, short):
        words = self._get_expansions(short)

        return words

    def shortify(self, word):
        start = word[0]
        end = word[-1]
        n = len(word) - 2

        return f"{start}{n}{end}"

    def shortify_sentence(self, sentence):
        assert sentence is not None

        shorties = []
        for word in sentence.split(" "):
            start = word[0]
            end = word[-1]
            n = len(word) - 2

            shorties.append(f"{start}{n}{end}")

        return shorties
