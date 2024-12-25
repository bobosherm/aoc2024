import sys
from contextlib import contextmanager


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
    n = 1000
    b_counter = dict()
    a_list = []
    for _ in range(n):
        a, b = [int(i) for i in input().split()]
        a_list.append(a)
        b_counter[b] = b_counter.get(b, 0) + 1
    res = 0
    for a in a_list:
        res += a * b_counter.get(a, 0)
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
