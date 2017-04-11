def verify_anagrams(first_word, second_word):
    first_word = ' '.join(x for x in first_word if x != ' ')
    second_word = ' '.join(x for x in second_word if x != ' ')
    return sorted(first_word.lower()) == sorted(second_word.lower())

