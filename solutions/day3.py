import sys
from contextlib import contextmanager
import re


@contextmanager
def fileio(enable):
    if enable:
        stdin = sys.stdin
        stdout = sys.stdout
        filein = open("input.txt", "r")
        fileout = open("output.txt", "w")
        sys.stdin = filein
        sys.stdout = fileout
    yield
    if enable:
        sys.stdin = stdin
        sys.stdout = stdout
        filein.close()
        fileout.close()


def solve():
    n = 6
    s = ""
    for _ in range(n):
        s += input()
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\s?\d+\)"
    ops = re.findall(pattern, s)
    do = True
    res = 0
    for op in ops:
        if op == "do()":
            do = True
        elif op == "don't()":
            do = False
        else:
            if do:
                a, b = [int(i) for i in op[4:-1].split(",")]
                res += a * b
    print(res)


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
