import unittest
from numeronym.numeronym import lexicon


class TestDictionary(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_words(self):
        words = lexicon.load_words()

        self.assertIsNotNone(words)
        self.assertGreater(len(words), 0)


if __name__ == "__main__":
    unittest.main()
