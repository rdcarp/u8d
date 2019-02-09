import argparse
import re
import sys

from .lexicon import load_words
from .parser import Parser
from . import __version__


def _get_parser():
    d = load_words()
    parser = Parser(d)

    return parser


def longify_randomly(args):
    assert "shorties" in args

    parser = _get_parser()

    longies = []
    for shortie in args.shorties.split(" "):
        longies.append(parser.longify_random(shortie))

    print(" ".join(longies))


def longify_list(args):
    assert "short" in args
    assert "n" in args
    parser = _get_parser()

    print(parser.longify_list(args.short)[0 : args.n + 1])


def shortify(args):
    parser = _get_parser()

    print(parser.shortify(args.word))


def shortify_sentence(args):
    assert "sentence" in args

    parser = _get_parser()
    print(" ".join(parser.shortify_sentence(args.sentence)))


def cludge(args):
    assert "sentence" in args

    parser = _get_parser()
    shorties = parser.shortify_sentence(args.sentence)
    print(" ".join([parser.longify_random(s) for s in shorties]))


def setup_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers()
    subparsers.required = False

    # 'cludge'
    cludge_parser = subparsers.add_parser("cludge")
    cludge_parser.set_defaults(func=cludge)
    cludge_parser.add_argument(dest="sentence", help="The starting sentence.")

    # 'shortify'
    shortify_parser = subparsers.add_parser("shortify")
    shortify_parser.set_defaults(func=shortify)
    shortify_parser.add_argument(dest="word", help="A 'long' word.")

    # 'shortify' sentence
    shortify_sentence_parser = subparsers.add_parser("shortify_sentence")
    shortify_sentence_parser.set_defaults(func=shortify_sentence)
    shortify_sentence_parser.add_argument(dest="sentence", help="The original sentence.")

    # 'longify' randomly
    longify_randonly_parser = subparsers.add_parser("longify_randomly")
    longify_randonly_parser.set_defaults(func=longify_randomly)
    longify_randonly_parser.add_argument(
        dest="shorties", help="A shortened form of a word or list of shortened forms."
    )

    # 'longify' list
    longify_list_parser = subparsers.add_parser("longify_list")
    longify_list_parser.set_defaults(func=longify_list)
    longify_list_parser.add_argument(dest="short", help="The shortened form of a word.")
    longify_list_parser.add_argument(
        "--number",
        "-n",
        dest="n",
        type=int,
        required=False,
        help="The maximum number of suggestions to make.",
        default="5",
    )

    parsed_args = parser.parse_args(args)

    if hasattr(parsed_args, "func"):
        return parsed_args.func(parsed_args)
    else:
        parser.print_help()
        return


if __name__ == "__main__":
    setup_args(sys.argv[1:])
