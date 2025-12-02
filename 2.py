import re
import sys
from typing import List

P1 = re.compile(r"^(\d+)\1$")
P2 = re.compile(r"^(\d+)\1+$")


def solveA(input: List[str]):
    ans = 0
    for i in input:
        x, y = i.split("-")
        for j in range(int(x), int(y) + 1):
            if P1.findall(str(j)):
                ans += j
    print(ans)


def solveB(input: List[str]):
    ans = 0
    for i in input:
        x, y = i.split("-")
        for j in range(int(x), int(y) + 1):
            if P2.findall(str(j)):
                ans += j
    print(ans)


if __name__ == "__main__":
    inp = [i.strip() for i in sys.stdin.readlines()][0].split(",")
    solveA(inp)
    print()
    solveB(inp)
