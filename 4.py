import re
import sys
from typing import List


def helper(input: List[str]):
    clone = [list(i) for i in input]
    m, n = len(input), len(input[0])
    ans = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] != "@":
                continue
            count = 0
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    a = x + j
                    b = y + k
                    if a >= 0 and a < m and b >= 0 and b < n and (k, j) != (0, 0):
                        count += input[a][b] == "@"
                    if count >= 4:
                        break
                if count >= 4:
                    break
            if count < 4:
                ans += 1
                clone[x][y] = "."
    return ans, clone


def solveA(input: List[str]):
    print(helper(input)[0])


def solveB(input: List[str]):
    ans = 0
    a, clone = helper(input)
    while clone != input:
        input = clone
        ans += a
        a, clone = helper(input)
    print(ans)


if __name__ == "__main__":
    inp = [i for i in sys.stdin.read().splitlines() if i]
    solveA(inp)
    print()
    solveB(inp)
