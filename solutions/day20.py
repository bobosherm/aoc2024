import sys
from contextlib import contextmanager
from queue import Queue
from itertools import combinations


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
    n = 141
    board = [input() for _ in range(n)]
    found = False
    for Y in range(n):
        for X in range(n):
            if board[Y][X] == "S":
                found = True
                break
        if found:
            break
    
    dist = {(Y, X): 0}
    q = Queue()
    q.put((Y, X))

    while not q.empty():
        y, x = q.get()
        for y_new, x_new in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            if 0 <= y_new < n and 0 <= x_new < n and board[y_new][x_new] != "#" and (y_new, x_new) not in dist:
                dist[(y_new, x_new)] = dist[(y, x)] + 1
                q.put((y_new, x_new))

    res = 0
    for ((y1, x1), s1), ((y2, x2), s2) in combinations(dist.items(), 2):
        d = abs(y2 - y1) + abs(x2 - x1)
        if d < 21 and s2 - s1 - d >= 100:
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
