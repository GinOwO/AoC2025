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
    raw_input = [i for i in sys.stdin.read().splitlines()]
    input = preprocess(raw_input)
    solveA(input, raw_input)
    print()
    solveB(input, raw_input)
