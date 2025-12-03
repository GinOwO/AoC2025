import re
import sys
from typing import List


def helper(s: str, x: int):
    num = pos = 0
    for i in range(-x + 1, 1):
        t = s[pos : len(s) + i]
        a = max(t)
        pos = pos + t.find(a) + 1
        num = num * 10 + int(a)
    return num


def solveA(input: List[str]):
    print(sum(helper(s, 2) for s in input))


def solveB(input: List[str]):
    print(sum(helper(s, 12) for s in input))


if __name__ == "__main__":
    inp = [i.strip() for i in sys.stdin.readlines() if i.strip()]
    solveA(inp)
    print()
    solveB(inp)
