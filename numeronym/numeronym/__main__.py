import fire
import re
from numeronym import dictionary
from numeronym.p4r import P4r


def _get_parser():
    d = dictionary.load_words()
    p4r = P4r(d)

    return p4r


def longify_randomly(short):
    p4r = _get_parser()

    longies = []
    for shortie in short.split(" "):
        longies.append(p4r.longify_random(shortie))

    print(" ".join(longies))


def longify_list(short_form, n):
    p4r = _get_parser()

    print(p4r.longify_list(short_form)[0 : n + 1])


def shortify(word):
    p4r = _get_parser()

    print(p4r.shortify(word))


def shortify_sentence(sentence):
    p4r = _get_parser()
    print(" ".join(p4r.shortify_sentence(sentence)))


def cludge(sentence):
    p4r = _get_parser()
    shorties = p4r.shortify_sentence(sentence)
    print(" ".join([p4r.longify_random(s) for s in shorties]))


def main():
    fire.Fire(
        {
            "longify_randomly": longify_randomly,
            "longify_list": longify_list,
            "shortify": shortify,
            "shortify_sentence": shortify_sentence,
            "cludge": cludge,
        }
    )


if __name__ == "__main__":
    main()
