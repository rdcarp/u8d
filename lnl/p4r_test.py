import unittest
from lnl.p4r import P4r

MOCK_DICTIONARY = ("never", "gonna", "give", "you", "up", "gave", "gunna")


class TestP4r(unittest.TestCase):
    def setUp(self):
        self.parser = P4r(MOCK_DICTIONARY)

    def test_expansion_length(self):
        word = self.parser.longify_random("g3a")

        expected = 5
        actual = len(word)

        self.assertEqual(expected, actual, "Expanded word not expected length")

    def test_expansion_list_length(self):
        words = self.parser.longify_list("g2e")

        expected = 2
        actual = len(words)

        self.assertEqual(expected, actual, "Did not get expected number of expansions")

    def test_generated_short_hand(self):
        word = "spam"

        expected = "s2m"
        actual = self.parser.shortify(word)

        self.assertEqual(expected, actual, "Word shortening did not match")

    def test_shortening_short_words(self):
        word = "if"
        expected = "i0f"

        actual = self.parser.shortify(word)

        self.assertEqual(expected, actual)

    def test_symbols_in_words(self):
        

if __name__ == "__main__":
    unittest.main()
