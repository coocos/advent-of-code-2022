from pathlib import Path


def parse_input() -> list[tuple[str, str]]:
    return [
        tuple(line.split(" "))
        for line in (Path(__file__).parent / "input.txt").read_text().splitlines()
    ]


def first(a: str, b: str) -> int:

    mapped = {"X": "A", "Y": "B", "Z": "C"}
    shape_score = {"A": 1, "B": 2, "C": 3}
    round_score = {
        "A": {
            "A": 3,
            "B": 0,
            "C": 6,
        },
        "B": {
            "A": 6,
            "B": 3,
            "C": 0,
        },
        "C": {"A": 0, "B": 6, "C": 3},
    }
    return round_score[mapped[b]][a] + shape_score[mapped[b]]


def second(a: str, b: str) -> int:

    mapped = {"X": "L", "Y": "D", "Z": "W"}
    need = {
        "A": {
            "W": "Y",
            "D": "X",
            "L": "Z",
        },
        "B": {
            "W": "Z",
            "D": "Y",
            "L": "X",
        },
        "C": {"W": "X", "D": "Z", "L": "Y"},
    }
    return first(a, need[a][mapped[b]])


def solve() -> None:

    hands = parse_input()

    # First part
    first_score = sum(first(opponent, you) for opponent, you in hands)
    assert first_score == 12794

    # Second part
    second_score = sum(second(opponent, you) for opponent, you in hands)
    assert second_score == 14979


if __name__ == "__main__":
    solve()
