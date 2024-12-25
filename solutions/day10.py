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
    n = 59
    board = [input() for _ in range(n)]

    def ok(i, j):
        return 0 <= i < n and 0 <= j < n
    
    q = Queue()
    for i in range(n):
        for j in range(n):
            if board[i][j] == "0":
                q.put((i, j))
    res = 0
    while not q.empty():
        i, j = q.get()
        if board[i][j] == "9":
            res += 1
            continue
        if ok(i-1, j) and board[i-1][j] == str(int(board[i][j]) + 1):
            q.put((i-1, j))
        if ok(i+1, j) and board[i+1][j] == str(int(board[i][j]) + 1):
            q.put((i+1, j))
        if ok(i, j-1) and board[i][j-1] == str(int(board[i][j]) + 1):
            q.put((i, j-1))
        if ok(i, j+1) and board[i][j+1] == str(int(board[i][j]) + 1):
            q.put((i, j+1))
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
