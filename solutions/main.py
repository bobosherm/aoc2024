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
    k = 7
    keys, locks = [], []
    for _ in range(n):
        board = [input() for _ in range(k)]
        input()
        pins = [-1] * 5
        for i in range(5):
            for j in range(k):
                if board[j][i] == "#":
                    pins[i] += 1
        if "." in board[0]:
            keys.append(pins)
        else:
            locks.append(pins)
    
    res = 0
    for key in keys:
        for lock in locks:
            stuck = False
            for i in range(5):
                if key[i] + lock[i] > k - 2:
                    stuck = True
            if not stuck:
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
