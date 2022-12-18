from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


Point = tuple[int, int, int]


def parse_input() -> set[Point]:

    cubes: set[Point] = set()
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        cubes.add(tuple(int(c) for c in line.split(",")))
    return cubes


def neighbours(point: Point) -> Iterable[Point]:

    for x, y, z in [
        (-1, 0, 0),
        (0, 0, -1),
        (1, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, -1, 0),
    ]:
        yield (point[0] + x, point[1] + y, point[2] + z)


def bubble(origin: Point, cubes: set[Point]) -> bool:

    visited = set([origin])
    queue = deque([origin])

    x_axis = list(sorted(cube[0] for cube in cubes))
    y_axis = list(sorted(cube[1] for cube in cubes))
    z_axis = list(sorted(cube[2] for cube in cubes))

    while queue:

        point = queue.popleft()
        if (
            point[0] == x_axis[0]
            or point[0] == x_axis[-1]
            or point[1] == y_axis[0]
            or point[1] == y_axis[-1]
            or point[2] == z_axis[0]
            or point[2] == z_axis[-1]
        ):
            return False

        for neighbour in neighbours(point):
            if neighbour not in visited and neighbour not in cubes:
                queue.append(neighbour)
                visited.add(neighbour)

    return True


def solve() -> None:

    cubes = parse_input()

    area = 0
    exterior = 0
    for cube in cubes:
        for neighbour in neighbours(cube):
            if neighbour not in cubes:
                area += 1
                if not bubble(neighbour, cubes):
                    exterior += 1

    # First part
    assert area == 4456

    # Second part
    assert exterior == 2510


if __name__ == "__main__":
    solve()
