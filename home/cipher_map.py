def recall_password(cipher_grille, ciphered_password):
    result = []
    for z in range(4):
        for pair in zip(cipher_grille, ciphered_password):
            for a, b in zip(*pair):
                if a == 'X':
                    result.append(b)
        cipher_grille = list(zip(*cipher_grille[::-1]))
    return ''.join(result)
