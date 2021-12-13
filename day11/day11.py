directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]  # right, left, down, up, diagonals


class Simulator:
    def __init__(self, grid):
        self.grid = grid
        self.flash_count = 0
        self.all_flashed = False

    def simulate(self, n):
        for i in range(n):
            self.simulate_day()
            print(f"after day {i+1}")
            self.print_grid()

    def simulate_until_all_flashed(self):
        count = 0
        while not self.all_flashed:
            count += 1
            self.simulate_day()
        print(f"flashed all after {count} steps")

    def simulate_day(self):
        self.increase_by_1()
        self.flash_all()

    def increase_by_1(self):
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.grid[y][x] += 1

    def flash_all(self):
        flashed_today = []
        for y, row in enumerate(self.grid):
            for x, n in enumerate(row):
                if n > 9 and (x, y) not in flashed_today:
                    self.flash(x, y, flashed_today)

        for x, y in flashed_today:
            self.grid[y][x] = 0

        if len(flashed_today) == len(self.grid) * len(self.grid[0]):
            self.all_flashed = True

    def flash(self, x, y, flashed_today):
        self.flash_count += 1
        flashed_today.append((x, y))
        for dx, dy in directions:
            x2, y2 = (x + dx, y + dy)
            if self.in_bounds(x2, y2):
                self.grid[y2][x2] += 1
                if self.grid[y2][x2] > 9 and (x2, y2) not in flashed_today:
                    self.flash(x2, y2, flashed_today)

    def print_grid(self):
        for line in self.grid:
            print("".join([str(n) for n in line]))
        print()

    def in_bounds(self, x, y):
        return y >= 0 and x >= 0 and y < len(self.grid) and x < len(self.grid[y])


def part_1(grid):
    sim = Simulator(grid)
    sim.simulate(100)
    print(f"total flash count: {sim.flash_count}")


def part_2(grid):
    sim = Simulator(grid)
    sim.simulate_until_all_flashed()


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    grid = [[int(c) for c in line] for line in lines]
    # part_1(grid)
    part_2(grid)
