from AvitoParser.config import TOKEN_WORDS, TOKEN_SYMBOLS


def links_filter(link):
    info_string = link[42:]
    flag = []
    for token_word in TOKEN_WORDS:
        if token_word in info_string:
            flag.append(1)
        else:
            flag.append(0)

    if sum(flag) == 0:
        return True
    else:
        return False


def replace_symbol(string):
    for symbol in TOKEN_SYMBOLS:
        string = string.replace(symbol, "")

    return string

