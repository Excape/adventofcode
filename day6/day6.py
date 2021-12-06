
from collections import Counter, deque

def simulate(input, days):
  counter = Counter(input)
  count_by_day = deque([counter[i] or 0 for i in range(9)])
  for d in range(days):
     spawning = count_by_day[0]
     count_by_day.rotate(-1)
     count_by_day[6] += spawning
     print(f"after {d+1} days: {sum(count_by_day)}")
  return count_by_day

with open('input6.txt') as f:
    lines = f.readlines()
    input = list(map(int, lines[0].split(',')))
    result = simulate(input, 256)
    print(sum(result))