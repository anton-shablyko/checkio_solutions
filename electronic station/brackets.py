def checkio(expression):
    s = ''.join(i for i in expression if i in '([{}])')

    while s:
        t, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == t:
            return False
    return True

checkio("(3+{1-1})")