VOWELS = "aeiouy"

def translate(phrase):
    i = 0
    result = ''
    while i < len(phrase):
        if phrase[i] in VOWELS:
            result += phrase[i]
            i += 3
        elif phrase[i] == ' ':
            result += phrase[i]
            i += 1
        else:
            result += phrase[i]
            i += 2

    print(result)

translate("hoooowe yyyooouuu duoooiiine")

