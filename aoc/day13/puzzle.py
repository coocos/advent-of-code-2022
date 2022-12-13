import json
from itertools import zip_longest
from functools import cmp_to_key
from math import prod
from pathlib import Path


def parse_input() -> list[tuple[list, list]]:
    pairs = []
    for pair in (Path(__file__).parent / "input.txt").read_text().split("\n\n"):
        first, second = pair.split("\n")
        pairs.append((json.loads(first), json.loads(second)))
    return pairs


def order(left: list, right: list) -> int:

    for x, y in zip_longest(left, right):
        match (x, y):
            case int(x), int(y):
                if x < y:
                    return -1
                elif x > y:
                    return 1
            case list(x), list(y):
                if (result := order(x, y)) != 0:
                    return result
            case list(x), int(y):
                if (result := order(x, [y])) != 0:
                    return result
            case int(x), list(y):
                if (result := order([x], y)) != 0:
                    return result
            case None, _:
                return -1
            case _, None:
                return 1
    return 0


def solve() -> None:

    pairs = parse_input()

    # First part
    right_indices = [
        i + 1 for i, (left, right) in enumerate(pairs) if order(left, right) == -1
    ]
    assert sum(right_indices) == 6428

    # Second part
    divider_packets = [[[2]], [[6]]]
    unordered = [*divider_packets]
    for left, right in pairs:
        unordered += [left, right]
    ordered = list(sorted(unordered, key=cmp_to_key(order)))
    decoder_key = prod(
        i + 1 for i, packet in enumerate(ordered) if packet in divider_packets
    )
    assert decoder_key == 22464


if __name__ == "__main__":
    solve()
