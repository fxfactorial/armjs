import math
import sys


def another_function():
    return 42


def program(value):
    c = value + 1
    d = c * 2
    a = d * 4
    return math.cos(c) + math.sin(c)


if __name__ == "__main__":
    program(sys.argv[1])
