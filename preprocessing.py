from stem import PorterStemmer


def lowercase_only(str):
    s = ""
    for ch in str:
        if ch.isalpha():
            s += ch.lower()
    return s


def cleanup_text(record):
    text = record[8]
    stop_words = []
    with open("stop_words.txt") as f:
        stop_words = f.readlines()
    stop_words = [x[:-1] for x in stop_words]
    output = [lowercase_only(token) for token in text.split()]
    ps = PorterStemmer()
    output = [ps.stem(word) for word in output if len(
        word) > 2 and word not in stop_words]
    return output
