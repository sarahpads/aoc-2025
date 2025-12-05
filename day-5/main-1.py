from pathlib import Path
from itertools import groupby

def parse_fresh_range(input) -> range:
  start, end = input.split("-")
  return range(int(start), int(end) + 1)

def is_fresh(ingredient: int, fresh_ranges: list[range]) -> bool:
  return any(ingredient in fresh_range for fresh_range in fresh_ranges)

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
    ingredients = [int(value) for value in sections[1]]

    fresh_ingredients = [ingredient for ingredient in ingredients if is_fresh(ingredient, fresh_ranges)]
    print(len(fresh_ingredients))

if __name__ == "__main__":
  main()
