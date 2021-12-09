def parse_line(line):
    patterns_output = line.split(" | ")
    return patterns_output[0].split(), patterns_output[1].split()


segment_counts = {2: 1, 4: 4, 3: 7, 7: 8}


def part_1(input):
    outputs = [i[1] for i in input]
    decoded_outputs = list(map(decode_output, outputs))
    return sum(len(line) for line in decoded_outputs)


def part_2(input):
    return list(map(map_patterns, input))


def map_patterns(patterns_output):
    patterns, outputs = patterns_output

    mappings = {segment_counts[len(p)]: p for p in patterns if len(p) in segment_counts}
    for p in patterns:
        if not len(p) in segment_counts:
            mappings[find_match(p, mappings)] = p

    return decode_outputs(mappings, outputs)


def find_match(pattern, fixed_mappings):
    l = len(pattern)
    if l == 6:  # 0 / 6 / 9
        if is_l(pattern, fixed_mappings[4]) == 4:
            return 9
        if is_l(pattern, fixed_mappings[7]) == 3:  # 0 / 6
            return 0
        return 6
    elif l == 5:  # 2 / 3 / 5
        if is_l(pattern, fixed_mappings[4]) == 2:
            return 2
        if is_l(pattern, fixed_mappings[7]) == 3:
            return 3
        return 5


def decode_outputs(mappings, outputs):
    inv_m = {sort(v): k for k, v in mappings.items()}
    digits = [str(inv_m[sort(out)]) for out in outputs]
    return int("".join(digits))


def sort(s):
    return "".join(sorted(s))


def is_l(p1, p2):
    return len(set(p1).intersection(p2))


def decode_output(output):
    return [segment_counts[len(o)] for o in output if len(o) in segment_counts]


with open("input.txt") as f:
    lines = f.readlines()
    input = list(map(parse_line, lines))
    part1_result = part_1(input)
    print(f"part 1: found {part1_result} digits")

    part2_result = part_2(input)
    print(f"part 2 sum: {sum(part2_result)}")
