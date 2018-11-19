import unittest
from lnl import dictionary, graphs


class TestShortyGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_shturf(self):
        words = dictionary.load_words()
        sg = graphs.ShortyGraph()

        for word in words:
            sg.add_word(word)

        longies = sg.lookup_shorty("b2b")
        print(longies)


if __name__ == "__main__":
    unittest.main()
