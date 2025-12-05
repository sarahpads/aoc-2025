from collections import deque
from pathlib import Path


OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def load_rows(path: Path) -> list[str]:
    with path.open() as fh:
        return [line.rstrip("\n") for line in fh]

def parse_rolls(rows: list[str]) -> set[tuple[int, int]]:
    return {
        (x, y)
        for y, row in enumerate(rows)
        for x, ch in enumerate(row)
        if ch == "@"
    }

def count_neighbours(rolls: set[tuple[int, int]], x: int, y: int) -> int:
    return sum((x + dx, y + dy) in rolls for dx, dy in OFFSETS)

def count_accessible(rolls: set[tuple[int, int]]) -> int:
    return sum(1 for x, y in rolls if count_neighbours(rolls, x, y) < 4)

def total_removed(rolls: set[tuple[int, int]]) -> int:
    neighbours = {pos: count_neighbours(rolls, *pos) for pos in rolls}
    queue = deque(pos for pos, count in neighbours.items() if count < 4)
    removed = 0

    while queue:
        pos = queue.popleft()
        if pos not in rolls:
            continue
        if neighbours[pos] >= 4:
            continue

        rolls.remove(pos)
        removed += 1

        x, y = pos
        for dx, dy in OFFSETS:
            neighbour = (x + dx, y + dy)
            if neighbour in rolls:
                neighbours[neighbour] -= 1
                if neighbours[neighbour] < 4:
                    queue.append(neighbour)

    return removed

def main() -> None:
    path = Path(__file__).with_name("input.txt")
    rows = load_rows(path)
    rolls = parse_rolls(rows)
    part2 = total_removed(set(rolls))
    print(part2)

if __name__ == "__main__":
    main()
