import re
import sys
from typing import List, Any


def solveA(input: List[Any]):
    intervals, nums = input

    ans = 0
    for z in nums:
        found = False
        for x, y in intervals:
            if x <= z <= y:
                found = True
                break
        ans += found
        i += 1

    print(ans)


def solveB(input: List[Any]):
    merged, _ = input
    total = sum(y - x + 1 for x, y in merged)
    print(total)


def preprocess(input: List[str]):
    intervals = []
    i = 0

    while input[i] != "":
        x, y = input[i].split("-")
        intervals.append([int(x), int(y)])
        i += 1
    i += 1

    intervals.sort()

    merged = [intervals[0]]
    for q in range(1, len(intervals)):
        if intervals[q][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[q][1])
        else:
            merged.append(intervals[q])

    nums = []
    for i in range(i, len(input)):
        nums.append(int(input[i]))

    return (merged, nums)


if __name__ == "__main__":
    inp = preprocess([i for i in sys.stdin.read().splitlines()])
    solveA(inp)
    print()
    solveB(inp)
