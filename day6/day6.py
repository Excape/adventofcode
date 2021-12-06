
def simulate_day(fishes):
  new_fish_count = 0
  for i, fish in enumerate(fishes):
    if fish["age"] == 0:
      fish["age"] = 6
      new_fish_count += fish["count"]
      
    else:
      fish["age"] -= 1

  if (new_fish_count):
    fishes.append({"age": 8, "count": new_fish_count})

with open('input6.txt') as f:
    lines = f.readlines()
    input = list(map(int, lines[0].split(',')))
    fishes = [{"age": i, "count": 1} for i in input]
    for d in range(256):
      simulate_day(fishes)
      # print(f"after day {d+1}: {fishes}")

    count_fishes = sum(f["count"] for f in fishes)
    print(f"there are {count_fishes} fishies")