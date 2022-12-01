from pathlib import Path


def parse_input() -> list[int]:
    calories = (Path(__file__).parent / "input.txt").read_text().split("\n\n")
    return list(
        sorted([sum(map(int, elf.splitlines())) for elf in calories], reverse=True)
    )


def solve() -> None:

    calories = parse_input()

    # First part
    assert calories[0] == 69836

    # Second part
    assert sum(calories[:3]) == 207968


if __name__ == "__main__":
    solve()
