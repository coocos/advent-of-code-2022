from pathlib import Path
from math import prod


def parse_input() -> list[list[int]]:
    return [
        [int(cell) for cell in list(line)]
        for line in (Path(__file__).parent / "input.txt").read_text().splitlines()
    ]


def solve() -> None:

    grid = parse_input()

    max_scenic_score = 0
    visible = len(grid) * 4 - 4

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid) - 1):
            origin = grid[y][x]

            left = list(reversed(grid[y][:x]))
            right = grid[y][x + 1 :]
            top = [row[x] for row in list(reversed(grid[:y]))]
            bottom = [row[x] for row in grid[y + 1 :]]

            scenic_scores = []
            for trees in [left, right, top, bottom]:
                scenic_scores.append(0)
                for tree in trees:
                    scenic_scores[-1] += 1
                    if tree >= origin:
                        break
            max_scenic_score = max(max_scenic_score, prod(scenic_scores))

            for trees in [left, right, top, bottom]:
                if all(tree < origin for tree in trees):
                    visible += 1
                    break

    # First part
    assert visible == 1851

    # Second part
    assert max_scenic_score == 574080


if __name__ == "__main__":
    solve()
