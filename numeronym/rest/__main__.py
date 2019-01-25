"""
REST API access to numeronym features.
"""

from bottle import route, run, template

from numeronym.numeronym.lexicon import load_words
from numeronym.numeronym.parser import Parser


class NumeronymRest:
    @route("/api/")
    def index():
        return {
            "maps": [
                {"url": "/cludge", "verbs": ["GET"]},
                {"url": "/shortify", "verbs": ["GET"]},
                {"url": "/longify", "verbs": ["GET"]},
            ]
        }

    @route("/api/cludge/<sentence>")
    def v1_cludge(sentence):
        p = Parser(load_words())
        shorties = p.shortify_sentence(sentence)
        result = " ".join([p.longify_random(s) for s in shorties])

        return {"original": sentence, "result": result}

    @route("/api/shortify/<sentence>")
    def v1_shortify(sentence):
        p = Parser(load_words())
        result = p.shortify_sentence(sentence)

        return {"original": sentence, "result": result}

    @route("/api/longify/<shorties>")
    def v1_longify(shorties):
        p = Parser(load_words())
        result = p.longify_random(shorties)

        return {"original": shorties, "result": result}

    def start(self):
        run(host="localhost", port=8086)


if __name__ == "__main__":
    app = NumeronymRest()
    app.start()
