from pathlib import Path

PATH = Path(__file__).with_name("input.txt")

joltages = []

def find_max_joltage(batteries):
  first_value = -1
  second_value = -1

  for index, battery in enumerate(batteries):
    if index == len(batteries) - 1 and battery > second_value:
      second_value = battery
      break
    elif battery > first_value:
      first_value = battery
      second_value = -1
    elif battery > second_value:
      second_value = battery

  return first_value * 10 + second_value

with open(PATH) as input:
  for line in input:
    batteries = [int(x) for x in list(line.strip('\n'))]

    joltage = find_max_joltage(batteries)

    joltages.append(joltage)

print(sum(joltages))