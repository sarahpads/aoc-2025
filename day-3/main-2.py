from pathlib import Path
from functools import reduce

PATH = Path(__file__).with_name("input.txt")

joltages = []

def find_max_joltage(batteries):
  values = [-1] * 12
  length = len(batteries)

  for index, battery in enumerate(batteries):
    # make sure we only consider changing indexes that we have enough numbers to fill
    start_index = max(0, 12 - length + index)

    for index, value in enumerate(values[start_index:]):
      if (battery > value):
        values[index + start_index] = battery
        # clear everything following this index, otherwise it changes the order of batteries
        values[index + start_index + 1:] = [-1] * (12 - (index + start_index + 1))
        break

  return reduce(lambda accum, battery: accum * 10 + battery, values, 0)

with open(PATH) as input:
  for line in input:
    batteries = [int(x) for x in list(line.strip('\n'))]

    joltage = find_max_joltage(batteries)

    joltages.append(joltage)
    print(joltage)

print(sum(joltages))