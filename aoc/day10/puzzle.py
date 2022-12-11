from pathlib import Path


def parse_input() -> list[str]:
    return (Path(__file__).parent / "input.txt").read_text().splitlines()


def solve() -> None:

    instructions = parse_input()
    x: int = 1
    cycles: list[int] = []

    for instruction in instructions:
        match instruction.split(" "):
            case ["addx", z]:
                cycles += [x, x + int(z)]
                x += int(z)
            case ["noop"]:
                cycles.append(x)

    # First part
    assert (
        sum(cycle * cycles[cycle - 2] for cycle in [20, 60, 100, 140, 180, 220])
        == 15020
    )

    pixels = [" "] * 240
    for i, x in enumerate(cycles):
        if (i + 1) % 40 in (x - 1, x, x + 1):
            pixels[i] = "#"

    # Second part
    for i, c in enumerate(pixels):
        print(c, end="")
        if (i + 1) % 40 == 0:
            print("")


if __name__ == "__main__":
    solve()
