en_lowercase_symbols = """qwertyuiop[]asdfghjkl;'zxcvbnm,./"""
en_uppercase_symbols = """QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?"""

ru_lowercase_symbols = """йцукенгшщзхъфывапролджэячсмитьбю."""
ru_uppercase_symbols = """ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"""


def create_table(language: str):
    if language == "ru":
        en_symbols = en_lowercase_symbols + en_uppercase_symbols
        ru_symbols = map(ord, ru_lowercase_symbols + ru_uppercase_symbols)

        return dict(zip(ru_symbols, en_symbols))

    en_symbols = map(ord, en_lowercase_symbols + en_uppercase_symbols)
    ru_symbols = ru_lowercase_symbols + ru_uppercase_symbols

    return dict(zip(en_symbols, ru_symbols))


while True:
    data = input("<text_language> <text>\n")

    text = data[3:]
    text_language = data[:2]

    table = create_table(text_language)

    print(text.translate(table))
