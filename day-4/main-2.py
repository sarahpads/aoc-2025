from pathlib import Path

PATH = Path(__file__).with_name("input.txt")

results = {}
rolls = 0

def increment_neighbour(key):
  if (results.get(key) is not None):
    results[key] += 1
    return 1
  else:
    return 0

def remove_rolls():
  doomed = [pos for pos in results.keys() if results.get(pos) < 4]

  for key in doomed:
    results.pop(key)

  return doomed

def count_neighbours(x, y):
  count = 0
  count += increment_neighbour((x - 1, y))
  count += increment_neighbour((x - 1, y - 1))
  count += increment_neighbour((x, y - 1))
  count += increment_neighbour((x + 1, y - 1))
  return count

with open(PATH) as input:
  for y, line in enumerate(input):
    for x, char in enumerate(line.strip('\n')):
      if (char != "@"):
        continue

      results[(x, y)] = count_neighbours(x, y)

  removed = remove_rolls()

  while (len(removed)):
    rolls += len(removed)

    for key in results.keys():
      x, y = key
      results[key] = count_neighbours(x, y)

    removed = remove_rolls()

print(rolls)
