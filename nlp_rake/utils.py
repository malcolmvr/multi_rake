import regex
from langdetect import detect_langs

LETTERS_RE = regex.compile(r'\p{L}+')

SENTENCE_DELIMITERS_RE = regex.compile(
    r'[\.,;:¡!¿\?…⋯‹›«»\\"“”\[\]\(\)⟨⟩}{&]'  # any punctuation sign or &
    r'|\s[-–~]+\s',  # or '-' between spaces
    regex.VERBOSE,
)


def detect_language(text, proba_threshold):
    try:
        proba_t = (proba_threshold / 100)
        for langprob in detect_langs(text):
            if langprob.prob > proba_t:
                return langprob.lang
    except Exception:
        return None


def keep_only_letters(string):
    return ' '.join(token.group() for token in LETTERS_RE.finditer(string))


def separate_words(text):
    words = []

    for word in text.split():
        if not word.isnumeric():
            words.append(word)

    return words


def split_sentences(text):
    sentences = SENTENCE_DELIMITERS_RE.split(text)
    return sentences
