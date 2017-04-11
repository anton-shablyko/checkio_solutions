def rotate(state, pipe_numbers):
    result = []
    holes = []
    """1'st"""
    # for _ in state:
    #     holes.append([(state[b]) for b in pipe_numbers])
    #     state = state[-1:] + state [:-1]
    #
    # result = [i for i, v in enumerate(holes) if sum(v) == len(v)]
    # print(result)
    # return result

    """2'nd"""
    for i, v in enumerate(state):
        x = [(state[b]) for b in pipe_numbers]
        if sum(x) == len(x):
            holes.append(i)
        state = state[-1:] + state [:-1]
    print(holes)
    return holes


rotate([1,0,0,0,1,1,0,1,0,0,0,1], [0, 1, 2])