from pathlib import Path
from itertools import islice

def main() -> None:
  # x coords of existing beams
  beams = {}

  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    for line in islice(input, 0, None, 2):
      for x, char in enumerate(line.rstrip("\n")):
        if char == "S":
          beams[x] = 1

        elif char == "^":
          split_beams = beams.pop(x, None)

          if not split_beams:
            continue

          beams[x - 1] = beams.get(x - 1, 0) + split_beams
          beams[x + 1] = beams.get(x + 1, 0) + split_beams

    print(sum(beams.values()))

if __name__ == "__main__":
  main()