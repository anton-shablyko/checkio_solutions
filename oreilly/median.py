def checkio(data):
    data.sort()
    if len(data) % 2 != 0:
        return data[int(len(data)/2)]
    else:
        x = int(len(data) / 2)
        return (data[x-1] + data[x])/2


checkio([3, 1, 2, 5, 4, 6])