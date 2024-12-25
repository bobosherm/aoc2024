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
        # sys.stdout = fileout
    yield
    if enable:
        sys.stdin = stdin
        sys.stdout = stdout
        filein.close()
        fileout.close()


def solve():
    n = 130
    board = [[i for i in input()] for _ in range(n)]

    found = False
    for Y in range(n):
        if found:
            break
        for X in range(n):
            if board[Y][X] == "^":
                found = True
                break
    
    def ok(y, x):
        return 0 <= y < n and 0 <= x < n
    
    res = 0
    # The most inefficient solution you'll see today. Runs for like 30 seconds.
    loop_threshhold = 10 ** 5
    for i in range(n):
        # For progress checking
        if i % 5 == 0 :
            print(">>", 100 * i // n)
        for j in range(n):
            if board[i][j] != ".":
                continue
            board[i][j] = "#"
            y, x = Y, X
            d = 0
            out = False
            for _ in range(loop_threshhold):
                if d == 0:
                    if not ok(y-1, x):
                        out = True
                        board[i][j] = "."
                        break
                    elif board[y-1][x] == "#":
                        d = 1
                    else:
                        y -= 1
                elif d == 1:
                    if not ok(y, x+1):
                        out = True
                        board[i][j] = "."
                        break
                    elif board[y][x+1] == "#":
                        d = 2
                    else:
                        x += 1
                elif d == 2:
                    if not ok(y+1, x):
                        out = True
                        board[i][j] = "."
                        break
                    elif board[y+1][x] == "#":
                        d = 3
                    else:
                        y += 1
                else:
                    if not ok(y, x-1):
                        out = True
                        board[i][j] = "."
                        break
                    elif board[y][x-1] == "#":
                        d = 0
                    else:
                        x -= 1
            if not out:
                res += 1
                board[i][j] = "."
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
