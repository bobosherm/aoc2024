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


def gcd(a, b):
    while a > 0:
        b %= a
        a, b = b, a
    return b


def solve():
    n = 50
    board = [[i for i in input()] for _ in range(n)]
    antennas = dict()
    antinodes = set()

    for i in range(n):
        for j in range(n):
            if board[i][j] != ".":
                antennas[board[i][j]] = antennas.get(board[i][j], []) + [(i, j)]
    
    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                y1, x1 = positions[i]
                y2, x2 = positions[j]
                max_steps = gcd(abs(y2 - y1), abs(x2 - x1))
                dy, dx = (y2 - y1) // max_steps, (x2 - x1) // max_steps

                y_, x_ = y1, x1
                while 0 <= y_ < n and 0 <= x_ < n:
                    antinodes.add((y_, x_))
                    y_ -= dy
                    x_ -= dx
                
                y_, x_ = y1, x1
                while 0 <= y_ < n and 0 <= x_ < n:
                    antinodes.add((y_, x_))
                    y_ += dy
                    x_ += dx
    
    print(len(antinodes))


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
