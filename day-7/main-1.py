from pathlib import Path
from itertools import islice

def main() -> None:
  # x coords of existing beams
  beams = set()
  splits = 0

  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    for line in islice(input, 0, None, 2):
      for x, char in enumerate(line.rstrip("\n")):
        if char == "S":
          beams.add(x)

        elif char == "^" and x in beams:
          beams.discard(x)
          beams.add(x - 1)
          beams.add(x + 1)
          splits += 1

    print(splits)

if __name__ == "__main__":
  main()