import sys
from contextlib import contextmanager
from itertools import permutations


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


num_pos = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}

dir_pos = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}


def get_paths(y_start, x_start, y_end, x_end, num=True):
    res = []
    blank = ((0, 0), (3, 0))[num]
    y_diff, x_diff = y_end - y_start, x_end - x_start

    if y_diff <= 0:
        steps = ("^", "v")[y_diff >= 0] * abs(y_diff) + ("<", ">")[x_diff >= 0] * abs(x_diff)
    else:
        steps = ("<", ">")[x_diff >= 0] * abs(x_diff) + ("^", "v")[y_diff >= 0] * abs(y_diff)
    # print(y_diff, x_diff, steps)
    combinations = list(set(permutations(steps)))
    for combination in combinations:
        y_current, x_current = y_start, x_start
        valid = True
        for c in combination:
            if c == "^":
                y_current -= 1
            elif c == "v":
                y_current += 1
            elif c =="<":
                x_current -= 1
            else:
                x_current += 1
            if (y_current, x_current) == blank:
                valid = False
                break
        if valid:
            res.append("".join(combination) + "A")
    
    return res
 
 
dp = dict()


def min_dirpad(path, d):
    if d == 0:
        return len(path)
    key = path + "_" + str(d)
    if key in dp:
        return dp[key]
    
    res = 0
    path = "A" + path
    for i in range(1, len(path)):
        y_prev, x_prev = dir_pos[path[i-1]]
        y, x = dir_pos[path[i]]
        paths = get_paths(y_prev, x_prev, y, x, False)
        res += min([min_dirpad(path, d - 1) for path in paths])
    
    dp[key] = res
    return res


def solve():
    n = 5
    d = 25
    res = 0
    
    for _ in range(n):
        inp = "A" + input()
        l = 0

        for i in range(1, len(inp)):
            y_prev, x_prev = num_pos[inp[i-1]]
            y, x = num_pos[inp[i]]
            paths = get_paths(y_prev, x_prev, y, x, True)
            l += min([min_dirpad(path, d) for path in paths])
        
        res += l * int(inp[1:-1])
    
    print(res)
 
 
def main():
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
