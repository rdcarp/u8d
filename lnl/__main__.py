import fire
import re
from lnl import dictionary
from lnl.p4r import P4r


def _get_parser():
    d = dictionary.load_words()
    p4r = P4r(d)
    p4r.load_graph(*d)

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


def uniques():
    p4r = _get_parser()
    uniques = []
    last_code = None

    for w in p4r.word_list:
        code = p4r.shortify(w)
        if code == last_code:
            break

        last_code = code
        if len(p4r.longify_list(code)) == 1:
            uniques.append(w)

    print(uniques)


def longify_list_graph(shorty):
    p = _get_parser()
    l = p.graph_longify(shorty)

    print(l)


def main():
    fire.Fire(
        {
            "longify_randomly": longify_randomly,
            "longify_list": longify_list,
            "shortify": shortify,
            "shortify_sentence": shortify_sentence,
            "cludge": cludge,
            "uniques": uniques,
            "longify_list_graph": longify_list_graph,
        }
    )


if __name__ == "__main__":
    main()
