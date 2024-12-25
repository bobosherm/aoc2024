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
    n = 75
    stones = dict()
    for i in input().split():
        stones[int(i)] = stones.get(int(i), 0) + 1
    
    for _ in range(n):
        new_stones = dict()
        for s, c in stones.items():
            if s == 0:
                new_stones[1] = new_stones.get(1, 0) + c
            elif len(str(s)) % 2 == 0:
                str_s = str(s)
                a, b = int(str_s[:len(str_s)//2]), int(str_s[len(str_s)//2:])
                new_stones[a] = new_stones.get(a, 0) + c
                new_stones[b] = new_stones.get(b, 0) + c
            else:
                new_stones[s * 2024] = new_stones.get(s * 2024, 0) + c
        stones = new_stones.copy()
    
    print(sum(new_stones.values()))


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
