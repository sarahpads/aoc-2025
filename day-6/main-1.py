from pathlib import Path
from re import sub
from functools import reduce

import operator

ops = {
  "+": operator.add,
  "*": operator.mul,
}

def solve_problem(problem: tuple[str, str, str, str]) -> int:
  numbers = [int(number) for number in problem[:-1]]
  operator = ops[problem[-1]]
  return reduce(operator, numbers)

def main() -> None:
  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    groups = [sub(" +", " ", line).split() for line in input]
    problems = zip(*groups)
    answers = [solve_problem(problem) for problem in problems]
    print(sum(answers))

if __name__ == "__main__":
  main()