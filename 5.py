import re
import sys
from typing import List


def solveA(input: List[str]):
    intervals = []

    i = 0
    while input[i] != "":
        x, y = input[i].split("-")
        intervals.append((int(x), int(y)))
        i += 1

    ans = 0
    i += 1

    while i < len(input):
        z = int(input[i])
        found = False
        for x, y in intervals:
            if x <= z <= y:
                found = True
                break
        ans += found
        i += 1

    print(ans)


def solveB(input: List[str]):
    intervals = []
    i = 0

    while input[i] != "":
        x, y = input[i].split("-")
        intervals.append([int(x), int(y)])
        i += 1

    intervals.sort()
    merged = [intervals[0]]

    for q in range(1, len(intervals)):
        if intervals[q][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[q][1])
        else:
            merged.append(intervals[q])

    total = sum(y - x + 1 for x, y in merged)
    print(total)


if __name__ == "__main__":
    inp = [i for i in sys.stdin.read().splitlines()]
    solveA(inp)
    print()
    solveB(inp)
