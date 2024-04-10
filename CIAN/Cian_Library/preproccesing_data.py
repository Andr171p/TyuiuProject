from CIAN.CianParser.config import WRONG_INFO


# this function filter info of ads:
def info_filter(info_string):
    flag = []
    for word in WRONG_INFO:
        if word in info_string.lower():
            flag.append(1)
        else:
            flag.append(0)

    return False if sum(flag) != 0 else True


# this function save only russian letters in string:
def string_to_sentence(text, mod):
    sentence = []
    match mod:
        case "info":
            for word in text.split():
                sentence.append(word)
            return ' '.join(sentence)
        case "area":
            for word in text.split():
                sentence.append(word)
            return float(sentence[3].replace(',', '.'))
        case "location":
            for word in text.split():
                sentence.append(word)
            sentence.pop(-1)
            sentence.pop(-1)
            return ' '.join(sentence)
        case "datetime":
            for word in text.split():
                sentence.append(word)
            sentence = sentence[1:]
            sentence[1] = sentence[1][:-1]
            return sentence[:-1]

