import sys
from typing import List


def solveA(input: List[str]):
    n = 50
    ans = 0
    for i in input:
        n = (n + (1, -1)[i[0] == "L"] * int(i[1:])) % 100
        ans += n == 0
    print(ans)


def solveB(input: List[str]):
    n = 50
    ans = 0
    for i in input:
        diff = n + (1, -1)[i[0] == "L"] * int(i[1:])
        if n and diff <= 0:
            ans += 1
        ans += abs(diff) // 100
        n = diff % 100
    print(ans)


if __name__ == "__main__":
    inp = [i.strip() for i in sys.stdin.readlines()]
    solveA(inp)
    print()
    solveB(inp)
