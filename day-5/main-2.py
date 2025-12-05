from pathlib import Path
from itertools import groupby

def parse_fresh_range(input) -> range:
  start, end = input.split("-")
  return range(int(start), int(end) + 1)

def main() -> None:
  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    rows = [line.rstrip("\n") for line in input]

    sections = [
      list(group)
      for is_blank, group in groupby(rows, key=lambda line: line == "")
      if not is_blank
    ]

    fresh_ranges = [parse_fresh_range(value) for value in sections[0]]
    id_ranges = sorted((r.start, r.stop - 1) for r in fresh_ranges)

    unique_ranges: list[tuple[int, int]] = []

    for start, end in id_ranges:
      if not unique_ranges:
        unique_ranges.append((start, end))
        continue

      current_start, current_end = unique_ranges[-1]

      if start <= current_end + 1:
        unique_ranges[-1] = (current_start, max(current_end, end))
      else:
        unique_ranges.append((start, end))

    print(sum([len(range(start, end + 1)) for start, end in unique_ranges]))

if __name__ == "__main__":
  main()
