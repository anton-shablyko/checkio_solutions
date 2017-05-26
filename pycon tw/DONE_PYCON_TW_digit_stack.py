def digit_stack(commands):
    stack = []
    _sum = 0
    for i in commands:
        if i == 'POP':  # Pop
            if stack:
                pop_val = stack.pop()
            else:
                pop_val = 0
            _sum += pop_val

        elif i == 'PEEK':  # Peek
            if stack:
                peek_val = stack[-1]
            else:
                peek_val = 0
            _sum += peek_val

        else:  # Push case
            num = int(i[-1])
            stack.append(num)
    return _sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
