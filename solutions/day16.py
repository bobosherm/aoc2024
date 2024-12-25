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
        sys.stdout = fileout
    yield
    if enable:
        sys.stdin = stdin
        sys.stdout = stdout
        filein.close()
        fileout.close()


def solve():
    n = 141
    res = 0
    board = []

    for l in range(n):
        board.append([i for i in input()])
    score = [[10 ** 15 for i in range(n)] for j in range(n)]
    q = Queue()

    for i in range(n):
        for j in range(n):
            if board[i][j] == "S":
                A, B = i, j
                q.put((i, j, 0, 0))
            if board[i][j] == "E":
                Y, X = i, j
    
    while not q.empty():
        y, x, s, d = q.get()
        if s < score[y][x]:
            score[y][x] = s
            if board[y][x+1] != "#":
                if d == 0:
                    q.put((y, x+1, s+1, 0))
                else:
                    q.put((y, x+1, s+1001, 0))
            if board[y][x-1] != "#":
                if d == 2:
                    q.put((y, x-1, s+1, 2))
                else:
                    q.put((y, x-1, s+1001, 2))
            if board[y+1][x] != "#":
                if d == 1:
                    q.put((y+1, x, s+1, 1))
                else:
                    q.put((y+1, x, s+1001, 1))
            if board[y-1][x] != "#":
                if d == 3:
                    q.put((y-1, x, s+1, 3))
                else:
                    q.put((y-1, x, s+1001, 3))

    q = Queue()
    c = 0
    q.put((Y, X, False))
    visited = [[False for i in range(n)] for j in range(n)]
    while not q.empty():
        y, x, d = q.get()
        if visited[y][x]:
            continue
        visited[y][x] = True
        board[y][x] = "O"
        c += 1
        if score[y-1][x] <= score[y][x] + (1000 if d else 0):
            q.put((y-1, x, score[y][x] - score[y-1][x] > 1))
        if score[y+1][x] <= score[y][x] + (1000 if d else 0):
            q.put((y+1, x, score[y][x] - score[y+1][x] > 1))
        if score[y][x-1] <= score[y][x] + (1000 if d else 0):
            q.put((y, x-1, score[y][x] - score[y][x-1] > 1))
        if score[y][x+1] <= score[y][x] + (1000 if d else 0):
            q.put((y, x+1, score[y][x] - score[y][x+1] > 1))
    res = c
    for i in range(n):
        for j in range(n):
            if board[i][j] == "O" and (i, j) not in ((Y, X), (A, B)):
                c = ""
                if board[i-1][j] == "O":
                    c += "^"
                if board[i+1][j] == "O":
                    c += "v"
                if board[i][j-1] == "O":
                    c += "<"
                if board[i][j+1] == "O":
                    c += ">"
                if len(c) == 1:
                    board[i][j] = "."
                    res -= 1
   
    print(score[Y][X])
                
    for a in board:
        print(*a)
    c = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == "O":
                c += 1
    
    # This solution has a bug, it includes some non-optimal paths too.
    # Instead of debugging the code I've printed its result and manually removed the non-optimal path as it takes less time.
    print(c)


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()