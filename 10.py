import re
import sys
import heapq
from typing import List, Any
from collections import deque
import numpy as np
import scipy.optimize


def solveA(input: List[Any], raw_input: List[str]):
    ans = 0

    for states, switches, _ in zip(*input):
        start = tuple([0] * len(states))
        goal = tuple(states)

        if start == goal:
            return 0

        q = deque([(start, 0)])
        seen = {start}
        res = None

        while q and res is None:
            state, d = q.popleft()
            pass
            for sw in switches:
                x = list(state)
                for k in sw:
                    x[k] ^= 1
                x = tuple(x)

                if x == goal:
                    res = d + 1
                    break

                if x not in seen:
                    seen.add(x)
                    q.append((x, d + 1))

        ans += res

    print(ans)


# Didnt know z3 existed b4 this :skull: so scipy it is
def solveB(input: List[Any], raw_input: List[str]):
    ans = 0

    for _, switches, joltages in zip(*input):
        n = len(joltages)
        m = len(switches)

        A_eq = np.zeros((n, m), dtype=int)
        for j, idxs in enumerate(switches):
            for k in idxs:
                A_eq[k, j] = 1

        c = np.ones(m, dtype=float)
        b_eq = np.array(joltages, dtype=int)
        bounds = [(0, None)] * m

        r = scipy.optimize.linprog(
            c=c,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            integrality=np.ones(m, dtype=int),
            method="highs",
        )

        ans += int(r.fun)
    print(ans)


def preprocess(input: List[str]):
    states = []
    switches = []
    joltage = []
    for line in input:
        state, *switch, jolt = line.split()
        states.append(list((i == "#") for i in state[1:-1]))
        switches.append([eval(f"[{s[1:-1]}]") for s in switch])
        joltage.append(eval(f"({jolt[1:-1]})"))
    return (states, switches, joltage)


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)

"""
...#.
#..##
.####
"""
