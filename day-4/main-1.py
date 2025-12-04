from pathlib import Path

PATH = Path(__file__).with_name("input.txt")

results = {}

def increment_neighbour(key):
  if (results.get(key) is not None):
    results[key] += 1
    return 1
  else:
    return 0

with open(PATH) as input:
  for y, line in enumerate(input):
    length = len(line.strip('\n'))

    for x, char in enumerate(line.strip('\n')):
      if (char != "@"):
        continue

      count = 0

      count += increment_neighbour((x - 1, y))
      count += increment_neighbour((x - 1, y - 1))
      count += increment_neighbour((x, y - 1))
      count += increment_neighbour((x + 1, y - 1))

      results[(x, y)] = count
      print((x, y), results[(x, y)])

print(sum(1 for value in results.values() if value < 4))