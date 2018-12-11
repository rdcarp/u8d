import argparse
import re
import sys

from numeronym.lexicon import load_words
from numeronym.parser import Parser
from numeronym import __version__


def _get_parser():
    d = load_words()
    parser = Parser(d)

    return parser


def longify_randomly(short):
    parser = _get_parser()

    longies = []
    for shortie in short.split(" "):
        longies.append(parser.longify_random(shortie))

    print(" ".join(longies))


def longify_list(short_form, n):
    parser = _get_parser()

    print(parser.longify_list(short_form)[0 : n + 1])


def shortify(word):
    parser = _get_parser()

    print(parser.shortify(word))


def shortify_sentence(sentence):
    parser = _get_parser()
    print(" ".join(parser.shortify_sentence(sentence)))


def cludge(sentence):
    parser = _get_parser()
    shorties = parser.shortify_sentence(sentence)
    print(" ".join([parser.longify_random(s) for s in shorties]))


def setup_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers()

    parser_cludge = subparsers.add_parser("cludge")
    parser_cludge.add_argument(
        "-s", "--sentence", help="The starting sentence", required=True
    )
    parser_cludge.set_defaults(func=cludge)

    parsed_args = parser.parse_args(args)
    parsed_args.func(parsed_args.sentence)


if __name__ == "__main__":
    # setup_args(sys.argv[1:])
    setup_args(("cludge", "-s", "the cat shat on the mat"))
