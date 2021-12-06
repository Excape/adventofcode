from functools import reduce


length = 12

def inverse_str(bin_str):
  return ''.join('1' if c == '0' else '0' for c in bin_str)

def to_int(bin_str):
  return int(bin_str, 2)

def part_1(input):
  gamma_str = "".join(
    ("1" if sum(int(n[i]) for n in input) > (len(input) / 2) else "0")
     for i in range(length)
  )
  eps_str = inverse_str(gamma_str)
  gamma = to_int(gamma_str)
  eps = to_int(eps_str)
  return gamma * eps

def filter_by_pos(candidates, i, filter_by):
  if (len(candidates) < 2):
    return list(candidates)

  s = sum(int(n[i]) for n in candidates)
  f = filter_by if s >= len(candidates) / 2 else inverse_str(filter_by)
  return filter(lambda n: n[i] == f, candidates)

def part_2(input):
  oxgen_rating = reduce(lambda c, i: filter_by_pos(c, i, "1"), range(length), input)
  co2_rating = reduce(lambda c, i: filter_by_pos(c, i, "0"), range(length), input)
  return to_int(oxgen_rating[0]) * to_int(co2_rating[0])

with open('input3.txt') as f:
    lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))