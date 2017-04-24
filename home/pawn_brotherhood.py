def safe_pawns(pawns):
    x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    safe = 0

    # generate possibly safe pairs
    def generate_pairs(x_val):
        x_ind = x_axis.index(x_val)
        try_1, try_2 = '', ''
        if x_ind == 0:  # if pawn on 'a' make sure we don't pick 'h' as a save field
            try_2 = x_axis[x_axis.index(x_val) + 1] + str(safe_y_val)
        elif x_ind == 7:
            try_1 = x_axis[x_axis.index(x_val) - 1] + str(safe_y_val)
        else:
            try_1 = x_axis[x_axis.index(x_val) - 1] + str(safe_y_val)
            try_2 = x_axis[x_axis.index(x_val) + 1] + str(safe_y_val)
        return try_1, try_2

    for i in pawns:
        x_val = i[0]
        safe_y_val = int(i[1]) - 1
        p1, p2 = generate_pairs(x_val)
        if p1 in pawns or p2 in pawns:
            safe += 1

    print(safe)
    return safe

#safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"])
#safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
#safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
safe_pawns(["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"])
