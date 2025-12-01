from pathlib import Path

positions = []
pointer = 50

PATH = Path(__file__).with_name("input.txt")

with open(PATH) as input:
  for line in input:
    direction = line[0]
    clicks = int(line[1:])
    modifier = 1 if direction == "R" else -1

    pointer = (pointer + clicks * modifier) % 100
    positions.append(pointer)

print(positions.count(0))