from __future__ import annotations
from dataclasses import dataclass
from itertools import pairwise
import re
from pathlib import Path


@dataclass
class Point:

    x: int
    y: int

    def distance(self, point: Point) -> int:
        return abs(self.x - point.x) + abs(self.y - point.y)


@dataclass
class Sensor:

    pos: Point
    beacon: Point


def parse_input() -> list[Sensor]:
    sensors = []
    pattern = (
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    for line in (Path(__file__).parent / "input.txt").read_text().splitlines():
        sx, sy, bx, by = re.match(pattern, line).groups()
        sensors.append(Sensor(Point(int(sx), int(sy)), Point(int(bx), int(by))))
    return sensors


def cannot_contain_beacon(sensors: list[Sensor], y: int) -> int:

    cannot_contain = set()
    for sensor in sensors:
        diff = abs(y - sensor.pos.y)
        if diff < sensor.pos.distance(sensor.beacon):
            start_x = sensor.pos.x - sensor.pos.distance(sensor.beacon) + diff
            stop_x = sensor.pos.x + sensor.pos.distance(sensor.beacon) - diff
            for x in range(start_x, stop_x):
                cannot_contain.add(x)

    return len(cannot_contain)


def tuning_frequency(sensors: list[Sensor], size: int = 20) -> int:

    for y in range(0, size + 1):
        ranges = []
        for sensor in sensors:
            diff = abs(y - sensor.pos.y)
            if diff < sensor.pos.distance(sensor.beacon):
                start_x = max(
                    0, sensor.pos.x - sensor.pos.distance(sensor.beacon) + diff
                )
                stop_x = min(
                    sensor.pos.x + sensor.pos.distance(sensor.beacon) - diff, size
                )
                ranges.append((start_x, stop_x))

        ranges.sort(key=lambda r: r[0])
        start_range = ranges[0]
        for a, b in ranges[1:]:
            if a > start_range[1] + 1:
                return y + (start_range[1] + 1) * 4_000_000
            start_range = (start_range[0], max(b, start_range[1]))

    return -1


def solve() -> None:

    sensors = parse_input()

    # First part
    assert cannot_contain_beacon(sensors, 2_000_000) == 5870800

    # Second part
    assert tuning_frequency(sensors, 4_000_000) == 10908230916597


if __name__ == "__main__":
    solve()
