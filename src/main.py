import math
import sys


def program(value):
    return math.cos(value) + math.sin(value)


if __name__ == "__main__":
    program(sys.argv[1])
