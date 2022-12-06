from pathlib import Path


def parse_input() -> str:
    return (Path(__file__).parent / "input.txt").read_text()


def marker(stream: str, size: int) -> int:
    for i in range(len(stream) - size - 1):
        if len(set(stream[i : i + size])) == size:
            return i + size
    return -1


def solve() -> None:

    stream = parse_input()

    # First part
    assert marker(stream, 4) == 1300

    # Second part
    assert marker(stream, 14) == 3986


if __name__ == "__main__":
    solve()
