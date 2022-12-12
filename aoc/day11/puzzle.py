from dataclasses import dataclass
from pathlib import Path
from collections import deque
from typing import Callable
from math import prod, lcm


@dataclass
class Monkey:

    items: deque[int]
    operation: Callable[[int], int]
    modulo: int
    next_true: int
    next_false: int
    inspections: int = 0


def parse_input() -> list[Monkey]:
    monkeys = []
    for section in (Path(__file__).parent / "input.txt").read_text().split("\n\n"):
        args = []
        for line in section.splitlines():
            match line.strip().replace(",", "").split(" "):
                case ["Starting", _, *items]:
                    args.append(deque([int(item) for item in items]))
                case ["Operation:", _, _, x, op, y]:
                    args.append(eval(f"lambda old: {x} {op} {y}"))
                case ["Test:", _, _, modulo]:
                    args.append(int(modulo))
                case ["If", "true:", _, _, _, other_monkey]:
                    args.append(int(other_monkey))
                case ["If", "false:", _, _, _, other_monkey]:
                    args.append(int(other_monkey))
        monkeys.append(Monkey(*args))
    return monkeys


def first() -> int:

    monkeys = parse_input()

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.operation(monkey.items.popleft()) // 3
                monkey.inspections += 1
                if item % monkey.modulo == 0:
                    monkeys[monkey.next_true].items.append(item)
                else:
                    monkeys[monkey.next_false].items.append(item)

    return prod(sorted((monkey.inspections for monkey in monkeys), reverse=True)[:2])


def second() -> int:

    monkeys = parse_input()

    for _ in range(10_000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.operation(monkey.items.popleft()) % prod(
                    monkey.modulo for monkey in monkeys
                )
                monkey.inspections += 1
                if item % monkey.modulo == 0:
                    monkeys[monkey.next_true].items.append(item)
                else:
                    monkeys[monkey.next_false].items.append(item)

    return prod(sorted((monkey.inspections for monkey in monkeys), reverse=True)[:2])


def solve() -> None:

    # First part
    assert first() == 101436

    # Second part
    assert second() == 19754471646


if __name__ == "__main__":
    solve()
