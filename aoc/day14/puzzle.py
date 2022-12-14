from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from itertools import pairwise


@dataclass(frozen=True)
class Point:

    x: int
    y: int


@dataclass
class Line:

    a: Point
    b: Point

    def points(self) -> Iterable[Point]:
        if self.a.x == self.b.x:
            for y in range(min(self.a.y, self.b.y), max(self.a.y, self.b.y) + 1):
                yield Point(self.a.x, y)
        else:
            for x in range(min(self.a.x, self.b.x), max(self.a.x, self.b.x) + 1):
                yield Point(x, self.a.y)


Grid = dict[Point, str]


def parse_input(with_floor: bool = False) -> Grid:

    grid: Grid = {}
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        points = [list(map(int, point.split(","))) for point in line.split(" -> ")]
        for a, b in pairwise(points):
            for point in Line(Point(*a), Point(*b)).points():
                grid[point] = "#"

    if with_floor:
        floor = max(point.y for point in grid.keys()) + 2
        for point in Line(Point(-1000, floor), Point(1000, floor)).points():
            grid[point] = "#"

    return grid


def drop_sand(grid: Grid, start: Point = Point(500, 0)) -> None:

    point = start
    abyss = max(point.y for point in grid.keys())

    while True:
        if point.y > abyss:
            break
        if (down := Point(point.x, point.y + 1)) not in grid:
            point = down
        elif (left := Point(point.x - 1, point.y + 1)) not in grid:
            point = left
        elif (right := Point(point.x + 1, point.y + 1)) not in grid:
            point = right
        else:
            grid[point] = "o"
            break


def solve() -> None:

    # First part
    grid = parse_input()
    previous_generations = set()
    while str(grid) not in previous_generations:
        previous_generations.add(str(grid))
        drop_sand(grid)

    assert sum(1 for cell in grid.values() if cell == "o") == 1078

    # Second part
    grid = parse_input(with_floor=True)
    while grid.get(Point(500, 0)) != "o":
        drop_sand(grid, start=Point(500, -1))

    assert sum(1 for cell in grid.values() if cell == "o") == 30157


if __name__ == "__main__":
    solve()
