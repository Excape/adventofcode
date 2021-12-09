def parse_boards(lines):
    boards = []
    current_board = []
    for line in lines:
        if line == "\n":
            boards.append(current_board)
            current_board = []
            continue
        row = filter(lambda c: c != "" and c != "\n", line.split(" "))
        row = list(map(int, row))
        current_board.append(row)
    boards.append(current_board)

    return boards


def init_marks(boards):
    return [
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        for _ in boards
    ]


def play_part1(boards, draw):
    marks = init_marks(boards)
    for n in draw:
        mark_boards(boards, marks, n)
        winner_i, winner_marks = get_winner(boards, marks)
        if winner_i:
            print(f"winner found: {winner_i}")
            return boards[winner_i], winner_marks, n
    raise ValueError("no winner found")


def play_part2(boards, draw):
    marks = init_marks(boards)
    for n in draw:
        mark_boards(boards, marks, n)
        if len(boards) == 1 and board_is_complete(marks[0]):
            return boards[0], marks[0], n
        remove_winners(boards, marks)

    raise ValueError("no board left")


def mark_boards(boards, marks, n):
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col == n:
                    marks[b][r][c] = 1


def pretty_print(boards):
    for b in boards:
        for row in b:
            print(*row)
        print("")


def get_winner(boards, marks):
    for b, board in enumerate(boards):
        if board_is_complete(marks[b]):
            return b, marks[b]
    return None, None


def remove_winners(boards, marks):
    to_remove = [i for i in range(len(boards)) if board_is_complete(marks[i])]
    for i in sorted(to_remove, reverse=True):
        del boards[i]
        del marks[i]


def board_is_complete(marks):
    cols = list(zip(*marks))  # transposed matrix

    for row in marks:
        if sum(row) == len(row):
            return True

    for col in cols:
        if sum(col) == len(col):
            return True

    return False


def calc_result(winner, marks, final_number):
    unmarked_sum = 0
    for r, row in enumerate(winner):
        for c, col in enumerate(row):
            if marks[r][c] == 0:
                unmarked_sum += col

    return unmarked_sum * final_number


with open("input4.txt") as f:
    lines = f.readlines()
    draw = list(map(int, lines[0].split(",")))
    boards = parse_boards(lines[2:])
    pretty_print(boards)

    winner, marks, final_number = play_part1(boards, draw)
    print(f"final n: {final_number}")
    result = calc_result(winner, marks, final_number)
    print(result)

    winner2, marks2, final_number2 = play_part2(boards, draw)
    print(f"final n: {final_number2}")
    result2 = calc_result(winner2, marks2, final_number2)
    print(result2)
