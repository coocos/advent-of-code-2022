import operator
from pathlib import Path


def parse_input() -> dict:
    monkeys = {}
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        match line.replace(":", "").split(" "):
            case [name, number]:
                monkeys[name] = int(number)
            case [name, first, operation, second]:
                monkeys[name] = (
                    first,
                    {
                        "+": operator.add,
                        "-": operator.sub,
                        "/": operator.floordiv,
                        "*": operator.mul,
                    }[operation],
                    second,
                )
    return monkeys


def yell(monkeys: dict, name: str) -> int:

    if type(monkeys[name]) == int:
        return monkeys[name]

    first, op, second = monkeys[name]
    return op(yell(monkeys, first), yell(monkeys, second))


def contains(monkeys: dict, name: str, target: str) -> bool:

    if type(monkeys[name]) == int:
        return name == target

    left, _, right = monkeys[name]
    return contains(monkeys, left, target) or contains(monkeys, right, target)


def need(monkeys: dict, name: str, target: int = 0):

    if type(monkeys[name]) == int:
        if name == "humn":
            return target
        return monkeys[name]

    left, op, right = monkeys[name]
    flipped = contains(monkeys, left, "humn")
    if op == operator.add:
        return (
            need(monkeys, left, target - yell(monkeys, right))
            if flipped
            else need(monkeys, right, target - yell(monkeys, left))
        )
    elif op == operator.sub:
        return (
            need(monkeys, left, target + yell(monkeys, right))
            if flipped
            else need(monkeys, right, yell(monkeys, left) - target)
        )
    elif op == operator.floordiv:
        return (
            need(monkeys, left, target * yell(monkeys, right))
            if flipped
            else need(monkeys, right, yell(monkeys, left) // target)
        )
    elif op == operator.eq:
        return (
            need(monkeys, left, yell(monkeys, right))
            if flipped
            else need(monkeys, right, yell(monkeys, left))
        )
    else:
        return (
            need(monkeys, left, target // yell(monkeys, right))
            if flipped
            else need(monkeys, right, target // yell(monkeys, left))
        )


def solve() -> None:

    monkeys = parse_input()

    # First part
    assert yell(monkeys, "root") == 22382838633806

    # Second part
    left, op, right = monkeys["root"]
    monkeys["root"] = (left, operator.eq, right)
    assert need(monkeys, "root") == 3099532691300


if __name__ == "__main__":
    solve()
