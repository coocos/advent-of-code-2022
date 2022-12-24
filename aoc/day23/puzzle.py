from collections import defaultdict, deque
from pathlib import Path
import sys


def parse_input() -> set[tuple[int, int]]:

    elves: set[tuple[int, int]] = set()
    lines = (Path(__file__).parent / "input.txt").read_text().splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                elves.add((int(x), int(y)))
    return elves


def solve() -> None:

    elves = parse_input()
    directions: deque[list[tuple[int, int]]] = deque(
        [
            [(-1, -1), (0, -1), (1, -1)],
            [(-1, 1), (0, 1), (1, 1)],
            [(-1, -1), (-1, 0), (-1, 1)],
            [(1, -1), (1, 0), (1, 1)],
        ]
    )

    empty_ground = 0

    for turn in range(sys.maxsize):

        propositions = defaultdict(list)
        for x, y in elves:
            if any(
                (x + xd, y + yd) in elves
                for xd, yd in [
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                ]
            ):
                for de, d, dw in directions:
                    if (
                        (x + de[0], y + de[1]) not in elves
                        and (x + d[0], y + d[1]) not in elves
                        and (x + dw[0], y + dw[1]) not in elves
                    ):
                        propositions[(x + d[0], y + d[1])].append((x, y))
                        break
                else:
                    propositions[(x, y)].append((x, y))
            else:
                propositions[(x, y)].append((x, y))

        next_gen = set()
        for next_pos, previous_pos in propositions.items():
            if len(previous_pos) > 1:
                next_gen.update(previous_pos)
            else:
                next_gen.add(next_pos)

        if turn == 10:
            xs = list(sorted(elf[0] for elf in elves))
            ys = list(sorted(elf[1] for elf in elves))
            for y in range(ys[0], ys[-1] + 1):
                for x in range(xs[0], xs[-1] + 1):
                    if (x, y) not in elves:
                        empty_ground += 1

        if elves == next_gen:
            break

        elves = next_gen
        directions.rotate(-1)

    # First part
    assert empty_ground == 4068

    # Second part
    assert turn + 1 == 968


if __name__ == "__main__":
    solve()
