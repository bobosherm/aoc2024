
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
    n, m = 50, 20
    res = 0
    board = []
    mapper = {
        ".": [".", "."],
        "O": ["[", "]"],
        "@": ["@", "."],
        "#": ["#", "#"]
    }

    for _ in range(n):
        row = []
        for i in input():
            row += mapper[i]
        board.append(row)
    
    input()
    moves = ""
    for i in range(m): moves += input()

    found = False
    for Y in range(n):
        for X in range(2*n):
            if board[Y][X] == '@':
                found = True
                break
        if found:
            break
    
    for m in moves:
        if m == "<":
            x = X
            while x > 0 and board[Y][x] not in (".", "#"):
                x -= 1
            if board[Y][x] == ".":
                while x < X:
                    board[Y][x], board[Y][x+1] = board[Y][x+1], board[Y][x]
                    x += 1
                X -= 1
        elif m == ">":
            x = X
            while x < 2 * n - 1 and board[Y][x] not in (".", "#"):
                x += 1
            if board[Y][x] == ".":
                while x > X:
                    board[Y][x], board[Y][x-1] = board[Y][x-1], board[Y][x]
                    x -= 1
                X += 1
        elif m == "^":
            y = Y
            to_move = [(Y, X)]
            movable = True
            move = []
            while len(to_move) > 0:
                y, x = to_move.pop()
                if [y, x] in move:
                    continue
                move.append([y, x])
                if board[y-1][x] == "#":
                    movable = False
                    break
                elif board[y-1][x] == "]":
                    to_move.append([y-1, x-1])
                    to_move.append([y-1, x])
                elif board[y-1][x] == "[":
                    to_move.append([y-1, x])
                    to_move.append([y-1, x+1])
            if movable:
                move.sort(key=lambda x: x[0])
                for y, x in move:
                    board[y][x], board[y-1][x] = board[y-1][x], board[y][x]
                Y -= 1
        else:
            y = Y
            to_move = [(Y, X)]
            movable = True
            move = []
            while len(to_move) > 0:
                y, x = to_move.pop()
                if [y, x] in move:
                    continue
                move.append([y, x])
                if board[y+1][x] == "#":
                    movable = False
                    break
                elif board[y+1][x] == "]":
                    to_move.append([y+1, x-1])
                    to_move.append([y+1, x])
                elif board[y+1][x] == "[":
                    to_move.append([y+1, x+1])
                    to_move.append([y+1, x])
            if movable:
                move.sort(key=lambda x: -x[0])
                for y, x in move:
                    board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
                Y += 1

    for i in range(n):
        for j in range(2*n-1):
            if board[i][j] == "[":
                res += 100 * i + min(j, 2*n-2)

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
