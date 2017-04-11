VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    def _split(text):
        pre_split = ''.join(i.upper() if (i.isalpha() or i.isdigit()) else ' ' for i in text)
        split = pre_split.split()
        return [i for i in split if len(i) > 1]
    text = _split(text)

    counter = 0
    for word in text:
        for i in range(len(word) - 1):
            _slice = word[i:i+2]
            if len(_slice) == 2:
                a = _slice[0]
                b = _slice[1]

            if (a in VOWELS and b in CONSONANTS) or (b in VOWELS and a in CONSONANTS):
                pass
            else:
                break
        else:
            counter += 1

    print(counter)
    return counter



#checkio("Dog,cat,mouse,bird.Human.")
checkio("A quantity of striped words")

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("My name is ...") == 3, "All words are striped"
#     assert checkio("Hello world") == 0, "No one"
#     assert checkio("A quantity of striped words.") == 1, "Only of"
#     assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
