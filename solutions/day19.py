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
    n = 400
    patterns = input().split(", ")
    res = 0

    input()
    for _ in range(n):
        design = input()
        k = len(design)
        dp = [0] * (k+1)
        dp[-1] = 1
        for i in range(k):
            if not dp[i-1]: continue
            for p in patterns:
                if i + len(p) <= k and design[i:i+len(p)] == p:
                    dp[i+len(p)-1] += dp[i-1]
        res += dp[-2]
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
