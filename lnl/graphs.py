class ShortyGraph:
    def __init__(self):
        self.root = {}

    def load_words(self, *words):
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        n = len(word) - 2
        start = word[0]
        end = word[-1]

        if start not in self.root:
            self.root[start] = {}

        if n not in self.root[start]:
            self.root[start][n] = {}

        if end not in self.root[start][n]:
            self.root[start][n][end] = []

        self.root[start][n][end].append(word)

    def lookup_shorty(self, shorty):
        start = shorty[0]
        end = shorty[-1]
        n = int(shorty[1:-1])

        return self.root.get(start, {}).get(n, {}).get(end, [])
