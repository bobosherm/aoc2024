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
    n, k = 1176, 1371 - 1177
    graph = set([input() for _ in range(n)])
    input()
    res = 0
    for _ in range(k):
        swaps = 0
        nums = [int(i) for i in input().split(",")]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if f"{nums[j]}|{nums[i]}" in graph:
                    nums[i], nums[j] = nums[j], nums[i]
                    swaps += 1
        if swaps > 0:
            res += nums[len(nums) // 2]
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
