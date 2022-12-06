from pathlib import Path
from collections import defaultdict


def parse_input() -> str:
    return (Path(__file__).parent / "input.txt").read_text()


def marker(stream: str, size: int) -> int:

    window: dict[str, int] = defaultdict(int)

    for tail in range(len(stream)):
        window[stream[tail]] += 1
        if (head := tail - size) >= 0:
            window[stream[head]] -= 1
            if window[stream[head]] == 0:
                del window[stream[head]]
        if len(window) == size:
            return tail + 1
    return -1


def solve() -> None:

    stream = parse_input()

    # First part
    assert marker(stream, 4) == 1300

    # Second part
    assert marker(stream, 14) == 3986


if __name__ == "__main__":
    solve()
