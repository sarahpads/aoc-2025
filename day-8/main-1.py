from math import dist, prod
from pathlib import Path
from itertools import combinations

def main() -> None:
  vectors = []
  path = Path(__file__).with_name("input.txt")

  with path.open() as input:
    for line in input:
      x, y, z = line.rstrip("\n").split(",")
      vectors.append((int(x), int(y), int(z)))


    pairs = sorted(combinations(vectors, 2), key=lambda pair: dist(pair[0], pair[1]))[:1000]

    circuits = []

    for pair in pairs:
      matching_circuits = [circuit for circuit in circuits if pair[0] in circuit or pair[1] in circuit]

      if (len(matching_circuits) == 2):
        matching_circuits[0].update(matching_circuits[1])
        circuits.remove(matching_circuits[1])

      elif (len(matching_circuits) == 1):
        matching_circuits[0].add(pair[0])
        matching_circuits[0].add(pair[1])

      else:
        circuits.append(set([pair[0], pair[1]]))

    biggest_circuits = sorted(circuits, key=len, reverse=True)[:3]

    print(prod(len(circuit) for circuit in biggest_circuits))

if __name__ == "__main__":
  main()