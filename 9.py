import math
import sys
from typing import List, Any
from collections import defaultdict


def solveA(input: List[Any], raw_input: List[str]):
    area = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            a = input[i]
            b = input[j]
            area = max(area, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
    print(area)


# i hate geometry
def solveB(input: List[Any], raw_input: List[str]):
    ans = 0
    n = len(input)

    for i in range(n):
        for j in range(i + 1, n):
            a = input[i]
            b = input[j]

            w = abs(a[0] - b[0]) + 1
            h = abs(a[1] - b[1]) + 1
            area = w * h

            if area <= ans:
                continue

            possible = True
            xmin, xmax = min(a[0], b[0]), max(a[0], b[0])
            ymin, ymax = min(a[1], b[1]), max(a[1], b[1])

            for a in range(n):
                b = (a + 1) % n
                x1, y1 = input[a]
                x2, y2 = input[b]

                if not (
                    (y1 >= ymax and y2 >= ymax)
                    or (y1 <= ymin and y2 <= ymin)
                    or (x1 >= xmax and x2 >= xmax)
                    or (x1 <= xmin and x2 <= xmin)
                ):
                    possible = False
                    break

            if possible:
                ans = area

    print(ans)


def preprocess(input: List[str]):
    val = [[int(i) for i in j.split(",")] for j in input]
    return val


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
