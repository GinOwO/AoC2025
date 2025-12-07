import re
import sys
from typing import List, Any
from functools import lru_cache


def solveA(input: List[Any], raw_input: List[str]):
    ans = 0
    for row in range(len(input)):
        for j in range(len(input[row])):
            touched = False
            if input[row][j] == "S":
                input[row + 1][j] = "|"
            if input[row][j] == "|":
                if row + 1 < len(input):
                    if input[row + 1][j] == "^":
                        if input[row + 1][j - 1] == ".":
                            touched = True
                            input[row + 1][j - 1] = "|"
                        if input[row + 1][j + 1] == ".":
                            touched = True
                            input[row + 1][j + 1] = "|"
                    else:
                        input[row + 1][j] = "|"
            ans += touched

    # print(*["".join(i) for i in input], sep="\n")
    print(ans)


def solveB(input: List[Any], raw_input: List[str]):
    for j in range(len(input[0])):
        if raw_input[0][j] == "S":
            break

    # ggz dp
    @lru_cache(None)
    def helper(i, j):
        if not (0 <= i < len(raw_input) and 0 <= j < len(raw_input[0])):
            return i == len(raw_input)

        ans = 0
        if raw_input[i][j] == "^":
            if raw_input[i][j - 1] == ".":
                ans += helper(i + 1, j - 1)
            if raw_input[i][j + 1] == ".":
                ans += helper(i + 1, j + 1)
        else:
            ans += helper(i + 1, j)
        return ans

    print(helper(1, j))


def preprocess(input: List[str]):
    return [list(i) for i in input]


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
