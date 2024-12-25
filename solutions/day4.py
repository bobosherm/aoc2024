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
    n = 140
    board = [input() for _ in range(n)]
    res = 0
    for i in range(n-2):
        for j in range(n-2):
            if board[i+1][j+1] + board[i][j] + board[i][j+2] + board[i+2][j] + board[i+2][j+2] in ("AMMSS", "ASSMM", "AMSMS", "ASMSM"):
                res += 1
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
