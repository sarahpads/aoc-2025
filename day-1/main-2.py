from pathlib import Path

zeros = 0
pointer = 50

PATH = Path(__file__).with_name("input.txt")

with open(PATH) as input:
  for line in input:
    direction = line[0]
    clicks = int(line[1:])
    modifier = 1 if direction == "R" else -1

    # how many times did we go past 0?
    zeros += clicks // 100

    # remainder
    new_pointer = (pointer + clicks * modifier) % 100

    if (pointer > 0 and pointer + (modifier * (clicks % 100)) not in range(1, 100)):
      zeros += 1

    pointer = new_pointer

print(zeros)
