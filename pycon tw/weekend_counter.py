from datetime import date, timedelta


def checkio(from_date, to_date):
    day_count = (to_date - from_date).days + 1
    # both list comprehensions can be merged into one. But this way is more readable and uder PEP regulations)
    x = [from_date + timedelta(n) for n in range(day_count)]
    y = [i for i in x if i.weekday() in (5, 6)]
    return len(y)