from pathlib import Path
from re import sub
from functools import reduce
from itertools import groupby
import operator

ops = {
  "+": operator.add,
  "*": operator.mul,
}

def batched(iterable):
  it = iter(iterable)
  chunk = []

  for piece in it:
    if (all(char.isspace() for char in piece)):
      yield chunk
      chunk = []
      continue
    chunk.append(piece)

  if chunk:
    yield chunk

def solve_problem(column):
  operator = ops[column[0][-1]]
  numbers = [
    int(digits)
    for row in column
    if (digits := sub(r"\D+", "", "".join(row)))
  ]
  return reduce(operator, numbers)

def main() -> None:
  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    answers = [solve_problem(column) for column in batched(zip(*input))]
    print(sum(answers))

if __name__ == "__main__":
  main()