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


def is_safe(nums):
    if len(nums) == 1:
        return True
    neg = nums[0] > nums[1]
    for i in range(1, len(nums)):
        if (nums[i] - nums[i-1]) * (1, -1)[neg] not in (1, 2, 3):
            return False
    return True


def solve():
    n = 1000
    res = 0
    for _ in range(n):
        nums = [int(i) for i in input().split()]
        if is_safe(nums):
            res += 1
            continue
        for i in range(n):
            if is_safe(nums[:i] + nums[i+1:]):
                res += 1
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
