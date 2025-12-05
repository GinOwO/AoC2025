import re
import sys
from typing import List, Any


def solveA(input: List[Any], raw_input: List[str]):
    pass


def solveB(input: List[Any], raw_input: List[str]):
    pass


def preprocess(input: List[str]):
    return input


if __name__ == "__main__":
    raw_inp = [i for i in sys.stdin.read().splitlines()]
    inp = preprocess(raw_inp)
    solveA(inp, raw_inp)
    print()
    solveB(inp, raw_inp)
