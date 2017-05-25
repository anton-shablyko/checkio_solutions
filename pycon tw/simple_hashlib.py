import hashlib


def checkio(hashed_string, algorithm):
    h = hashlib.new(algorithm)
    h.update(bytes(hashed_string, 'utf-8'))
    return h.hexdigest()

checkio('welcome', 'md5')