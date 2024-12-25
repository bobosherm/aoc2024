import sys
from contextlib import contextmanager
from queue import Queue


@contextmanager
def fileio(enable):
    if enable:
        stdin = sys.stdin
        stdout = sys.stdout
        filein = open("input.txt", "r")
        fileout = open("output.txt", "w")
        sys.stdin = filein
        # sys.stdout = fileout
    yield
    if enable:
        sys.stdin = stdin
        sys.stdout = stdout
        filein.close()
        fileout.close()


def solve():
    n = 71
    k = 3450
    res = 0
    board = [[True if i < n and j < n else False for i in range(n+1)] for j in range(n+1)]

    for i in range(k):
        # For progress checking
        if i % 100 == 0:
            print(">>", 100 * i // k)
        
        x, y = [int(i) for i in input().split(",")]
        X, Y = x, y
        board[y][x] = False
    
        costs = [[10 ** 10 for i in range(n)] for j in range(n)]
        q = Queue()
        q.put((0, 0, 0))

        while not q.empty():
            x, y, s = q.get()
            # print(x, y)
            if not board[y][x]:
                continue
            if board[y][x] and s < costs[y][x]:
                costs[y][x] = s
                q.put((x-1, y, s+1))
                q.put((x+1, y, s+1))
                q.put((x, y-1, s+1))
                q.put((x, y+1, s+1))
        
        if costs[n-1][n-1] == 10 ** 10:
            print(X, Y)
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
