from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class FileNode:

    name: str
    size: int


@dataclass
class DirectoryNode:

    name: str
    children: list[FileNode | DirectoryNode] = field(default_factory=list)

    @property
    def size(self) -> int:
        return sum(child.size for child in self.children)

    def subdirectories(self) -> Iterable[DirectoryNode]:
        for child in self.children:
            if isinstance(child, DirectoryNode):
                yield child
                yield from child.subdirectories()


def parse_input() -> list[tuple[str]]:
    return [
        tuple(line.split(" "))
        for line in (Path(__file__).parent / "input.txt").read_text().splitlines()
    ]


def create_file_system(commands: list[tuple[str]]) -> DirectoryNode:

    root = DirectoryNode("/")
    stack = [root]

    for command in commands:
        match command:
            case ("$", "cd", "/"):
                stack = [root]
            case ("$", "cd", ".."):
                stack.pop()
            case ("$", "cd", directory):
                stack.append(
                    next(
                        child
                        for child in stack[-1].children
                        if isinstance(child, DirectoryNode) and child.name == directory
                    )
                )
            case ("$", "ls"):
                continue
            case ("dir", directory):
                stack[-1].children.append(DirectoryNode(directory))
            case (size, name):
                stack[-1].children.append(FileNode(name, int(size)))

    return root


def solve() -> None:

    commands = parse_input()

    root = create_file_system(commands)

    # First part
    assert (
        sum(
            size
            for directory in root.subdirectories()
            if (size := directory.size) < 100_000
        )
        == 1307902
    )

    # Second part
    assert (
        min(
            size
            for directory in root.subdirectories()
            if (size := directory.size) >= (30_000_000 - (70_000_000 - root.size))
        )
        == 7068748
    )


if __name__ == "__main__":
    solve()
