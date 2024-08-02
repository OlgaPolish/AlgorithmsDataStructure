import string
from collections import Counter
from string import ascii_lowercase as lt


def find_letters(text):
    cnt = Counter()
    for letter in lt:
        cnt[letter] = text.count(letter)
    return dict(cnt)


def read_file(path):
    with open(path, encoding="utf8") as file:
        text = file.read().lower()
        spec_chars = string.punctuation + "\n\xa0«»\t—…\’\ "
        result = "".join([ch for ch in text if ch not in spec_chars])
    return result


print(find_letters(read_file('Test_text.txt')))
