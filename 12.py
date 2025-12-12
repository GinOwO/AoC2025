import re
import sys
from typing import List, Any

P = re.compile(r"(\d+)")

stk_placed = []


def revert(space, present):
    places = stk_placed.pop()
    for x, y in places:
        if space[x][y] != present:
            raise
        space[x][y] = -1


def rotate90(mat):
    return tuple([tuple(row) for row in zip(*mat[::-1])])


def rotate180(mat):
    return tuple([tuple(row[::-1]) for row in mat[::-1]])


def rotate270(mat):
    return rotate90(rotate180(mat))


def all_rotations(mat):
    return set(
        (tuple(tuple(i) for i in mat), rotate90(mat), rotate180(mat), rotate270(mat))
    )


def attempt_fit(x, y, space, present, presents):
    pp = presents[present]
    for rot in pp:
        placed = []
        possible = True
        for i in range(len(rot)):
            for j in range(len(rot[i])):
                if not rot[i][j]:
                    continue
                a, b = x + i, y + j
                if a >= len(space) or b >= len(space[0]) or space[a][b] != -1:
                    possible = False
                    break
                placed.append((a, b))
                space[a][b] = present
            if not possible:
                break
        if possible:
            stk_placed.append(placed)
            return True
        for a, b in placed:
            if space[a][b] == present:
                space[a][b] = -1
    return False


def solveA(input: List[Any], raw_input: List[str]):
    ans = 0
    presents = []
    _presents, spaces = input
    cc = [0] * len(_presents)
    for i, p in enumerate(_presents):
        # presents.append(all_rotations(p))
        presents.append(p)
        cc[i] = sum(sum(q) for q in p)

    def helper(x, y, counts, space):
        if all(p == 0 for p in counts):
            return 1

        if x >= len(space):
            return 0

        if y >= len(space[0]):
            return helper(x + 1, 0, counts, space)

        if space[x][y] != -1:
            while y < len(space[x]) and space[x][y] != -1:
                y += 1
            return helper(x, y, counts, space)

        if space[x][y] == -1:
            for p in range(len(counts)):
                if counts[p] == 0:
                    continue
                if attempt_fit(x, y, space, p, presents):
                    counts[p] -= 1
                    if helper(x, y + 1, counts, space):
                        return 1
                    revert(space, p)
                    counts[p] += 1

        return helper(x, y + 1, counts, space)

    for kk, i in enumerate(spaces):
        print(f"on space {kk}/{len(spaces)}")
        # # from a time of brutus, this wont finish
        # stk_placed.clear()
        # space = [[-1] * i[0][0] for _ in range(i[0][1])]
        # ans += helper(0, 0, i[1], space)
        x, y = i[0]
        ans += x * y > sum(a * b for a, b in zip(i[1], cc))
    print(ans)


def solveB(input: List[Any], raw_input: List[str]):
    print("Yay")


def preprocess(input: List[str]):
    presents = []
    i = 0
    while i < len(input):
        if "x" in input[i]:
            break
        if input[i] and input[i][0].isdigit():
            presents.append([])
        elif input[i]:
            presents[-1].append([int(j == "#") for j in input[i]])
        i += 1
    spaces = []
    for j in input[i:]:
        x = [int(i) for i in P.findall(j)]
        spaces.append([(x[0], x[1]), x[2:]])
    return presents, spaces


if __name__ == "__main__":
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
