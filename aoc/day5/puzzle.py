import re
from copy import deepcopy
from pathlib import Path


def parse_input() -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    crates, moves = (Path(__file__).parent / "input.txt").read_text().split("\n\n")
    crate_count = int(crates[-1][-1])

    stacks = [[] for _ in range(crate_count)]
    for line in crates.splitlines()[:-1]:
        for x in range(1, len(line), 4):
            if line[x].strip():
                stacks[x // 4].append(line[x])

    pattern = r"move (\d+) from (\d+) to (\d+)"
    return [list(reversed(stack)) for stack in stacks], [
        tuple(int(x) for x in re.match(pattern, move).groups())
        for move in moves.splitlines()
    ]


def solve() -> None:

    crates, moves = parse_input()

    # First part
    lifo_crates = deepcopy(crates)
    for amount, start, stop in moves:
        lifo_crates[stop - 1] += list(reversed(lifo_crates[start - 1][-amount:]))
        lifo_crates[start - 1] = lifo_crates[start - 1][:-amount]
    top_crates = "".join(crate[-1] for crate in lifo_crates)
    assert top_crates == "TLNGFGMFN"

    # Second part
    fifo_crates = deepcopy(crates)
    for amount, start, stop in moves:
        fifo_crates[stop - 1] += fifo_crates[start - 1][-amount:]
        fifo_crates[start - 1] = fifo_crates[start - 1][:-amount]
    top_crates = "".join(crate[-1] for crate in fifo_crates)
    assert top_crates == "FGLQJCMBD"


if __name__ == "__main__":
    solve()
