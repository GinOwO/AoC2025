import re
import sys
from typing import List, Any
from itertools import zip_longest


def solveA(input: List[Any], raw_input: List[str]):
    ans = 0
    nums, ops = input
    for j in range(len(ops)):
        col = ops[j] == "*"
        for i in range(len(nums)):
            if ops[j] == "*":
                col *= nums[i][j]
            else:
                col += nums[i][j]
        ans += col
    print(ans)


def solveB(input: List[Any], raw_input: List[str]):
    _, ops = input
    ans = 0
    m = 0

    ll = [int("".join(i).strip() or -1) for i in zip_longest(*raw_input[:-1])]
    nums = [[] for _ in range(len(ops))]

    for num in ll:
        if num != -1:
            nums[m].append(num)
        else:
            m += 1

    for j in range(len(ops)):
        col = ops[j] == "*"
        for num in nums[j]:
            if ops[j] == "*":
                col *= num
            else:
                col += num
        ans += col
    print(ans)


def preprocess(input: List[str]):
    nums = []
    operator = []
    for _i in input:
        nums.append([])
        for i in _i.split(" "):
            if not i:
                continue
            if not i.isnumeric():
                operator.append(i)
            else:
                nums[-1].append(int(i))
    nums.pop()
    return (nums, operator)


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
