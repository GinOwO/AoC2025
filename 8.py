import re
import sys
from typing import List, Any
from heapq import heapify, heappush, heappop
from math import prod

N = 1000


class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self, i):
        if self.Parent[i] != i:
            self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    # Unites the set that includes i and the set that
    # includes j by size
    def add(self, i, j):

        # Find the representatives (or the root nodes) for
        # the set that includes i
        irep = self.find(i)

        # And do the same for the set that includes j
        jrep = self.find(j)

        # Elements are in the same set, no need to unite
        # anything.
        if irep == jrep:
            return

        # Get the size of i’s tree
        isize = self.Size[irep]

        # Get the size of j’s tree
        jsize = self.Size[jrep]

        # If i’s size is less than j’s size
        if isize < jsize:

            # Then move i under j
            self.Parent[irep] = jrep

            # Increment j's size by i's size
            self.Size[jrep] += self.Size[irep]

        # Else if j’s size is less than i’s size
        else:
            self.Parent[jrep] = irep
            self.Size[irep] += self.Size[jrep]


def dist3d(pA, pB):
    return ((pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2 + (pA[2] - pB[2]) ** 2) ** 0.5


def solveA(input: List[Any], raw_input: List[str]):
    dist = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            heappush(dist, (dist3d(input[i], input[j]), i, j))
    dsu = DSU(len(input))

    for _ in range(N):
        item = heappop(dist)
        dsu.add(item[1], item[2])
    ans = sorted((i for i in dsu.Size if i > 1), reverse=True)
    print(ans[0] * ans[1] * ans[2])


def solveB(input: List[Any], raw_input: List[str]):
    dist = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            heappush(dist, (dist3d(input[i], input[j]), i, j))

    dsu = DSU(len(input))
    remaining = len(input)
    last_merge = None

    while remaining > 1:
        d, i, j = heappop(dist)
        ri = dsu.find(i)
        rj = dsu.find(j)

        if ri != rj:
            dsu.add(i, j)
            last_merge = (i, j)
            remaining -= 1

    x1 = input[last_merge[0]][0]
    x2 = input[last_merge[1]][0]
    print(x1 * x2)


def preprocess(input: List[str]):
    points = []
    for j in input:
        points.append([int(i) for i in j.split(",")])
    return points


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
