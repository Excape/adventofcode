from functools import reduce

neighbors = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]  # right, left, down, up, diagonals


def part_1(algo, source):
    enhanced = reduce(lambda img, n: enhance_img(algo, img, n), range(2), source)
    print_img(enhanced)
    count_lit = sum(len(list(filter(lambda p: p == "#", row))) for row in enhanced)
    print(f"there are {count_lit} pixels lit up")


def part_2(algo, source):
    enhanced = reduce(lambda img, n: enhance_img(algo, img, n), range(50), source)
    print_img(enhanced)
    count_lit = sum(len(list(filter(lambda p: p == "#", row))) for row in enhanced)
    print(f"there are {count_lit} pixels lit up")


def pad_image(img, infinity_p):
    empty_row = [infinity_p for _ in range(len(img[0]) + 2)]
    padded_img = list(map(lambda r: [infinity_p] + r[:] + [infinity_p], img))
    padded_img.insert(0, empty_row)
    padded_img.append(empty_row[:])
    return padded_img


def enhance_img(algo, img, nth_iter):
    infinity_p = get_infinite_pixel(algo, nth_iter)
    padded_img = pad_image(img, infinity_p)
    img_copy = [row[:] for row in padded_img]
    for y, row in enumerate(padded_img):
        for x, _ in enumerate(row):
            img_copy[y][x] = translate(padded_img, algo, infinity_p, x, y)
    return img_copy


def print_img(img):
    for row in img:
        print(*row)
    print()


def get_infinite_pixel(algo, nth_iter):
    if algo[0] == "." or nth_iter == 0:
        return "."
    if nth_iter % 2 == 1:
        return algo[0]
    return algo[-1]


def translate(img, algo, infinity_p, x, y):
    bit_map = list(
        map(
            lambda dx_dy: get_pixel(img, x + dx_dy[0], y + dx_dy[1], infinity_p),
            neighbors,
        )
    )
    bin_list = list(map(lambda p: 1 if p == "#" else 0, bit_map))
    bin_str = "".join(map(str, bin_list))
    bin_nr = int(bin_str, 2)
    return algo[bin_nr]


def get_pixel(img, x, y, infinity_p):
    if x >= 0 and y >= 0 and y < len(img) and x < len(img[0]):
        return img[y][x]
    return infinity_p


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    algo = lines[0]
    source_img = [[c for c in line] for line in lines[2:]]
    # part_1(algo, source_img)
    part_2(algo, source_img)
