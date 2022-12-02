from pathlib import Path


def parse_input() -> list[tuple[str, str]]:
    return [
        tuple(line.split(" "))
        for line in (Path(__file__).parent / "input.txt").read_text().splitlines()
    ]


def first(a: str, b: str) -> int:
    return {
        "X": {
            "A": 3,
            "B": 0,
            "C": 6,
        },
        "Y": {
            "A": 6,
            "B": 3,
            "C": 0,
        },
        "Z": {"A": 0, "B": 6, "C": 3},
    }[b][a] + {"X": 1, "Y": 2, "Z": 3}[b]


def second(a: str, b: str) -> int:
    return first(
        a,
        {
            "A": {
                "Z": "Y",
                "Y": "X",
                "X": "Z",
            },
            "B": {
                "Z": "Z",
                "Y": "Y",
                "X": "X",
            },
            "C": {"Z": "X", "Y": "Z", "X": "Y"},
        }[a][b],
    )


def solve() -> None:

    hands = parse_input()

    # First part
    assert sum(first(a, b) for a, b in hands) == 12794

    # Second part
    assert sum(second(a, b) for a, b in hands) == 14979


if __name__ == "__main__":
    solve()
