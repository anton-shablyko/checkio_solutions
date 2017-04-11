import math
def checkio(a, b, c):
    if a == b == c:
        return [60,60,60]
    elif (a+b <= c or a+c <= b or b+c <= a):
        return [0,0,0]
    else:
        result = []
        x = (b**2 + c**2 - a**2)/(2 * b * c)
        x = round(math.degrees(math.acos(x)))
        y = (a**2 + c**2 - b**2)/(2 * a * c)
        y = round(math.degrees(math.acos(y)))
        z = 180 - x - y
        result.append(x)
        result.append(y)
        result.append(z)
        return sorted(result)
