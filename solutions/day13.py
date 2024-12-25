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
    n = 320
    res = 0

    for _ in range(n):
        x1, y1 = [int(i[1:]) for i in input().split(": ")[1].split(", ")]
        x2, y2 = [int(i[1:]) for i in input().split(": ")[1].split(", ")]
        tx, ty = [int(i[2:]) for i in input().split(": ")[1].split(", ")]
        tx += 10 ** 13
        ty += 10 ** 13
        input()
        
        determinant = x1 * y2 - x2 * y1
        if determinant == 0:
            if x1 * ty == y1 * tx and x2 * ty == y2 * tx:
                # Infinite solutions, minimize.
                if x2 != 0:
                    find_b = lambda a: (tx - x1 * a) / x2
                    a_candidates = range(0, int(tx / x1) + 1) if x1 != 0 else [0]
                elif y2 != 0:
                    find_b = lambda a: (ty - y1 * a) / y2
                    a_candidates = range(0, int(ty / y1) + 1) if y1 != 0 else [0]
                else: 
                    continue

                min_cost = 10 ** 20
                for a in a_candidates:
                    b = find_b(a)
                    if b.is_integer() and a >= 0 and b >= 0:
                        b = int(b)
                        cost = 3 * a + b
                        min_cost = min(min_cost, cost)
                if min_cost != 10 ** 20:
                    res +=  min_cost
        else:
            # Cramer's Rule
            a = (tx * y2 - ty * x2) / determinant
            b = (x1 * ty - y1 * tx) / determinant
            if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
                res +=  int(3 * a + b)
    
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
