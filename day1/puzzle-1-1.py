with open("input1.txt") as f:
    lines = f.readlines()
    numbers = list(map(int, lines))
    print(sum(n[1] > n[0] for n in zip(numbers, numbers[1:])))
