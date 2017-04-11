def checkio(first, second):
    result = [i for i in first.split(",") if i in second.split(",")]
    return ','.join(sorted(result))
