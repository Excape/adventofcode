def window_sum(lines, last_i):
    return sum(lines[last_i - 2 : last_i + 1])


with open("input1.txt") as f:
    lines = f.readlines()
    numbers = list(map(int, lines))
    count = sum(
        window_sum(numbers, i) > window_sum(numbers, i - 1)
        for i in range(3, len(numbers))
    )

    print(count)
