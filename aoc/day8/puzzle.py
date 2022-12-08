from pathlib import Path


def parse_input() -> list[list[int]]:
    return [
        [int(cell) for cell in list(line)]
        for line in (Path(__file__).parent / "input.txt").read_text().splitlines()
    ]


def solve() -> None:

    grid = parse_input()

    best = 0
    count = len(grid) * 4 - 4
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid) - 1):
            origin = grid[y][x]

            left = list(reversed(grid[y][:x]))
            right = grid[y][x + 1 :]
            top = [row[x] for row in list(reversed(grid[:y]))]
            bottom = [row[x] for row in grid[y + 1 :]]

            left_score = 0
            for cell in left:
                left_score += 1
                if cell >= origin:
                    break

            right_score = 0
            for cell in right:
                right_score += 1
                if cell >= origin:
                    break

            top_score = 0
            for cell in top:
                top_score += 1
                if cell >= origin:
                    break

            bottom_score = 0
            for cell in bottom:
                bottom_score += 1
                if cell >= origin:
                    break
            best = max(best, left_score * right_score * bottom_score * top_score)

            if all(cell < origin for cell in left):
                count += 1
                continue
            if all(cell < origin for cell in right):
                count += 1
                continue
            if all(cell < origin for cell in top):
                count += 1
                continue
            if all(cell < origin for cell in bottom):
                count += 1
                continue

    assert count == 1851
    assert best == 574080


if __name__ == "__main__":
    solve()
