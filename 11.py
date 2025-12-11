import re
import sys
from typing import List, Any, DefaultDict, Set
from collections import defaultdict
from functools import lru_cache


def solveA(input: DefaultDict[int, Set], raw_input: List[str]):
    @lru_cache(None)
    def helper(curr):
        if curr == "out":
            return 1
        ans = 0
        for nxt in input[curr]:
            ans += helper(nxt)
        return ans

    print(helper("you"))


def solveB(input: List[Any], raw_input: List[str]):
    masks = defaultdict(int)
    masks["fft"] = 1
    masks["dac"] = 2

    @lru_cache(None)
    def helper(curr, mask=0):
        if curr == "out":
            return mask == 3

        ans, mask = 0, mask | masks[curr]
        for nxt in input[curr]:
            ans += helper(nxt, mask)
        return ans

    print(helper("svr"))


def preprocess(input: List[str]):
    graph = defaultdict(set)
    for x in input:
        i, v = x.split(":")
        for j in v.split():
            if j:
                graph[i].add(j)
    return graph


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
