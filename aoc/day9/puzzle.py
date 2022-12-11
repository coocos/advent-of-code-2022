from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


def parse_input() -> list[tuple[tuple[int, int], int]]:

    directions = {"R": (1, 0), "U": (0, -1), "D": (0, 1), "L": (-1, 0)}
    commands = []
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        direction, amount = line.split(" ")
        commands.append((directions[direction], int(amount)))
    return commands


def simulate_rope(commands: list[tuple[tuple[int, int], int]], knot_count: int) -> int:

    knots: list[tuple[int, int]] = [(0, 0)] * knot_count
    visited: set[tuple[int, int]] = set([(0, 0)])

    for direction, steps in commands:
        for _ in range(steps):

            knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])

            for i, knot in enumerate(knots):
                if i == 0:
                    continue

                prev = knots[i - 1]

                xd = prev[0] - knot[0]
                yd = prev[1] - knot[1]

                if abs(xd) != 2 and abs(yd) != 2:
                    continue

                if xd != 0:
                    xd /= abs(xd)
                if yd != 0:
                    yd /= abs(yd)

                knots[i] = (knot[0] + xd, knot[1] + yd)

            visited.add(knots[-1])

    return len(visited)


def solve() -> None:

    commands = parse_input()

    assert simulate_rope(commands, 2) == 6332

    assert simulate_rope(commands, 10) == 2511


if __name__ == "__main__":
    solve()
