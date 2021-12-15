from functools import reduce
from collections import Counter
import time


def measure(func):
  def inner(*args, **kwargs):
    t = time.process_time_ns()
    func(*args, **kwargs)
    elapsed_time = time.process_time_ns() - t
    print(f"Executed in {elapsed_time/10**6} ms")
  return inner

def parse_input(lines):
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        pattern_result = line.split(" -> ")
        rules[pattern_result[0]] = pattern_result[1]
    return template, rules


def part_1(template, rules):
    n = 10
    polymer = reduce(
        lambda poly, _: pair_insertion_bruteforce(poly, rules), range(n), template
    )
    counter = Counter(polymer)
    print(f"length: {len(polymer)}")
    print(counter)
    result = counter.most_common()[0][1] - counter.most_common()[-1][1]
    print(f"result: {result}")

@measure
def part_2(template, rules):
    pairs = [f"{p[0]}{p[1]}" for p in zip(template, template[1:])]
    counter = Counter(pairs)
    n = 400
    result_counter = reduce(
        lambda c, _: pair_insertion_smart(c, rules), range(n), counter
    )
    # count only first elements of pairs + the last one, which always stays the same
    occs = count_elements(result_counter, template[-1])
    result = max(occs.values()) - min(occs.values())
    print(occs)
    print(f"result: {result}")


def pair_insertion_smart(counter, rules):
    result = {}
    for pair, n in counter.items():
        insert = rules[pair]
        pair1 = f"{pair[0]}{insert}"
        pair2 = f"{insert}{pair[1]}"
        result[pair1] = n + result.get(pair1, 0)
        result[pair2] = n + result.get(pair2, 0)
    return result


def count_elements(counter, last_elem):
    occs = {}
    items = list(counter.items())
    for pair, n in counter.items():
        occs[pair[0]] = n + occs.get(pair[0], 0)

    occs[last_elem] += 1
    return occs


def pair_insertion_bruteforce(template, rules):
    pairs = [f"{p[0]}{p[1]}" for p in zip(template, template[1:])]
    inserts = []
    for i, pair in enumerate(pairs):
        if pair in rules:
            inserts.append((i, rules[pair]))
    return insert_elements(template, inserts)


def insert_elements(template, inserts):
    offset = 0
    polymer = template
    for i, c in inserts:
        p = i + offset + 1
        polymer = polymer[:p] + c + polymer[p:]
        offset += 1
    return polymer


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    template, rules = parse_input(lines)
    #part_1(template, rules)
    part_2(template, rules)
