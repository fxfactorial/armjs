import math
import sys


def program(value):
    c = value + 1
    return math.cos(c) + math.sin(c)


if __name__ == "__main__":
    program(sys.argv[1])
