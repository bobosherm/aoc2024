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
    n = 500
    a, b = 103, 101
    ps = []
    vs = []
    for _ in range(n):
        p, v = [[int(i) for i in j[2:].split(",")] for j in input().split()]
        ps.append(p)
        vs.append(v)
    
    found = False
    for i in range(20 ** 6):
        if found:
            break
        board = [["." for i in range(b)] for _ in range(a)]
        for j in range(n):
            p, v = ps[j], vs[j]
            x = (p[0] + i * v[0]) % b
            y = (p[1] + i * v[1]) % a
            board[y][x] = "1"
        for row in board:
            if "11111111" in "".join(row):
                found = True
                for row in board:
                    print("".join(row))
                print(i)
                break


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
