from __future__ import annotations
from dataclasses import dataclass
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

    xs = []
    for sensor in sensors:
        xs += [sensor.pos.x, sensor.beacon.x]
    xs = list(sorted(xs))

    max_distance = 0
    for sensor in sensors:
        max_distance = max(max_distance, sensor.pos.distance(sensor.beacon))

    cannot_contain = 0
    for x in range(xs[0] - max_distance, xs[-1] + max_distance):
        for sensor in sensors:
            # One beacon exists here so this point can contain by default
            if sensor.beacon.x == x and sensor.beacon.y == y:
                break

            distance_here = abs(sensor.pos.x - x) + abs(sensor.pos.y - y)
            distance_closest = abs(sensor.pos.x - sensor.beacon.x) + abs(
                sensor.pos.y - sensor.beacon.y
            )
            if distance_here <= distance_closest:
                cannot_contain += 1
                break

    return cannot_contain


def solve() -> None:

    sensors = parse_input()
    for sensor in sensors:
        print(sensor)

    assert cannot_contain_beacon(sensors, 2_000_000) == 5870800


if __name__ == "__main__":
    solve()
