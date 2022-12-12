import string
import sys
from pathlib import Path
from collections import deque
from typing import Iterable

Grid = list[list[int]]
Point = tuple[int, int]


def parse_input() -> tuple[Point, Point, Grid]:

    grid = []
    start = (-1, -1)
    stop = (-1, -1)
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        cols = list(line)
        for x, col in enumerate(cols):
            if col == "S":
                cols[x] = "a"
                start = (x, len(grid))
            elif col == "E":
                cols[x] = "z"
                stop = (x, len(grid))
        grid.append([string.ascii_lowercase.index(c) for c in cols])
    return (start, stop, grid)


def next_positions(pos: Point, grid: Grid) -> Iterable[Point]:

    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if (
            0 <= pos[0] + x < len(grid[0])
            and 0 <= pos[1] + y < len(grid)
            and grid[pos[1] + y][pos[0] + x] <= grid[pos[1]][pos[0]] + 1
        ):
            yield (pos[0] + x, pos[1] + y)


def fewest_steps(start: Point, stop: Point, grid: Grid) -> int:

    queue: deque[tuple[Point, int]] = deque([(start, 0)])
    visited = set([start])
    while queue:
        pos, steps = queue.popleft()
        if pos == stop:
            return steps
        for next_pos in next_positions(pos, grid):
            if next_pos not in visited:
                queue.append((next_pos, steps + 1))
                visited.add(next_pos)
    return sys.maxsize


def solve() -> None:

    start, stop, grid = parse_input()

    # First part
    steps = fewest_steps(start, stop, grid)
    assert steps == 497

    # Second part
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                steps = min(steps, fewest_steps((x, y), stop, grid))
    assert steps == 492


if __name__ == "__main__":
    solve()
