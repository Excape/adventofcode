from dataclasses import dataclass


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    @classmethod
    def from_input(cls, input):
        lines = []
        for l in input:
            start_end = l.split(" -> ")
            start = start_end[0].split(",")
            end = start_end[1].split(",")
            lines.append(cls(int(start[0]), int(start[1]), int(end[0]), int(end[1])))

        return lines

    def is_straight(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def get_spanning_coords(self):
        cords = [(self.x1, self.y1), (self.x2, self.y2)]
        x, y = self.x1, self.y1
        while x < self.x2:
            x += 1
            if y < self.y2:
                y += 1
            elif y > self.y2:
                y -= 1
            cords.append((x, y))
        while x > self.x2:
            x -= 1
            if y > self.y2:
                y -= 1
            elif y < self.y2:
                y += 1
            cords.append((x, y))
        while y < self.y2:
            y += 1
            cords.append((x, y))
        while y > self.y2:
            y -= 1
            cords.append((x, y))

        return list(set(cords))


def plot_lines(lines, straight_only):
    grid_size = 1000
    grid = [[0] * grid_size for _ in range(grid_size)]
    straight_lines = list(filter(lambda l: l.is_straight(), lines))
    input_lines = straight_lines if straight_only else lines
    for line in input_lines:
        coords = line.get_spanning_coords()
        for x, y in coords:
            grid[y][x] += 1

    return grid


def count_overlapping(grid):
    return sum(n > 1 for row in grid for n in row)


def pretty_print(grid):
    for row in grid:
        print(*row)
    print("")


with open("input.txt") as f:
    input = f.readlines()
    lines = Line.from_input(input)
    grid = plot_lines(lines, False)
    pretty_print(grid)
    count = count_overlapping(grid)
    print(f"there are {count} overlaps")
