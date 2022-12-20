from collections import deque
from pathlib import Path


def parse_input() -> list[tuple[int, int]]:

    return [
        (int(number), id)
        for id, number in enumerate(
            (Path(__file__).parent / "input.txt").read_text().splitlines()
        )
    ]


def coordinates(numbers: list[tuple[int, int]], rounds: int) -> int:

    mixed = deque(numbers)

    for _ in range(rounds):
        for number in numbers:
            while mixed[0] != number:
                mixed.rotate(1)
            mixed.popleft()
            mixed.rotate(-number[0])
            mixed.appendleft(number)

    while mixed[0][0] != 0:
        mixed.rotate(1)

    coordinate_sum = 0
    for cycle in range(3001):
        if cycle in (1000, 2000, 3000):
            coordinate_sum += mixed[0][0]
        mixed.rotate(-1)
    return coordinate_sum


def solve() -> None:

    numbers = parse_input()

    # First part
    assert coordinates(numbers, rounds=1) == 9945

    # Second part
    assert (
        coordinates([(number * 811589153, id) for number, id in numbers], rounds=10)
        == 3338877775442
    )


if __name__ == "__main__":
    solve()
