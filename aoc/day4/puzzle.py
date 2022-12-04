from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Assignment:

    start: int
    stop: int

    def contains(self, other: Assignment) -> bool:
        return (
            self.start <= other.start <= self.stop
            and self.start <= other.stop <= self.stop
        )

    def overlaps(self, other: Assignment) -> bool:
        return (
            self.start <= other.start <= self.stop
            or self.start <= other.stop <= self.stop
        )


def parse_input() -> list[tuple[Assignment, Assignment]]:
    pairs: list[tuple[Assignment, Assignment]] = []
    lines = (Path(__file__).parent / "input.txt").read_text().splitlines()
    for line in lines:
        first, second = [
            tuple(int(section) for section in sections.split("-"))
            for sections in line.split(",")
        ]
        pairs.append((Assignment(*first), Assignment(*second)))
    return pairs


def solve() -> None:

    pairs = parse_input()

    # First part
    assert sum(1 for a, b in pairs if a.contains(b) or b.contains(a)) == 542

    # Second part
    assert sum(1 for a, b in pairs if a.overlaps(b) or b.overlaps(a)) == 900


if __name__ == "__main__":
    solve()
