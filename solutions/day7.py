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
    n = 850
    calibration = 0
    for c in range(n):
        # For progress checking
        if c % 50 == 0:
            print(">>", 100 * c // n)
        
        target, nums = input().split(":")
        target = int(target)
        nums = nums.split()
        len_nums = [len(i) for i in nums]
        nums = [int(i) for i in nums]
        for i in range(3 ** len(nums) - 1):
            op = i
            res = nums[0]
            for j in range(1, len(nums)):
                match op % 3:
                    case 0: res += nums[j]
                    case 1: res *= nums[j]
                    case 2: res = res * 10 ** len_nums[j] + nums[j]
                op //= 3
            if res == target:
                calibration += target
                break
    print(calibration)


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
