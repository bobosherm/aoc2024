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
    n = 140
    board = [input() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    res = 0
    q = Queue()
    
    def ok(x, y):
        return 0 <= x < n and 0 <= y < n
        
    q.put((0, 0))
    # For the entire grid
    while not q.empty():
        current_shape = [[False] * (n+1) for _ in range(n+1)]
        p, a = 0, 0
        # For each shape
        while not q.empty():
            x, y = q.get()
            if visited[x][y]:
                continue
            val = board[x][y]
            visited[x][y] = True
            current_shape[x][y] = True
            a += 1
            # Add adjecent cells within the same shape
            if ok(x-1, y) and board[x-1][y] == val and not visited[x-1][y]:
                q.put((x-1, y))
            if ok(x, y-1) and board[x][y-1] == val and not visited[x][y-1]:
                q.put((x, y-1))
            if ok(x+1, y) and board[x+1][y] == val and not visited[x+1][y]:
                q.put((x+1, y))
            if ok(x, y+1) and board[x][y+1] == val and not visited[x][y+1]:
                q.put((x, y+1))
        # Count sides
        for x in range(n):
            for y in range(n):
                    if current_shape[x][y]:
                        if not current_shape[x-1][y]:
                            left = current_shape[x][y-1] and not current_shape[x-1][y-1]
                            if not left:
                                p += 1
                        if not current_shape[x+1][y]:
                            left = current_shape[x][y-1] and not current_shape[x+1][y-1]
                            if not left:
                                p += 1
                        if not current_shape[x][y-1]:
                            left = current_shape[x-1][y] and not current_shape[x-1][y-1]
                            if not left:
                                p += 1
                        if not current_shape[x][y+1]:
                            left = current_shape[x-1][y] and not current_shape[x-1][y+1]
                            if not left:
                                p += 1
        res += p * a
        
        # Find a new shape
        for i in range(n * n):
            x, y = i // n, i % n
            if not visited[x][y]:
                q.put((x, y))
                break
        
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
