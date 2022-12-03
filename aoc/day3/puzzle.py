import string
from pathlib import Path
from typing import Iterable


def parse_input() -> list[str]:
    return (Path(__file__).parent / "input.txt").read_text().splitlines()


priorities = {item: i + 1 for i, item in enumerate(string.ascii_letters)}


def priorities_per_sack(rucksacks: list[str]) -> Iterable[int]:

    for sack in rucksacks:
        a, b = sack[: len(sack) // 2], sack[len(sack) // 2 :]
        for item in set(a) & set(b):
            yield priorities[item]


def priorities_per_group(rucksacks: list[str]) -> Iterable[int]:

    while rucksacks:
        a, b, c = [set(sack) for sack in rucksacks[:3]]
        yield priorities[(a & b & c).pop()]
        rucksacks = rucksacks[3:]


def solve() -> None:

    rucksacks = parse_input()

    # First part
    assert sum(priorities_per_sack(rucksacks)) == 7785

    # Second part
    assert sum(priorities_per_group(rucksacks)) == 2633


if __name__ == "__main__":
    solve()
