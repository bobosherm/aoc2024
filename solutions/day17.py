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


def run(A, B, C, instructions):
    def get_combo(k):
        if k < 4:
            return k
        return (A, B, C)[k-4]
    
    res = []
    i = 0
    c = 0
    while i < len(instructions):
        c += 1
        if c > 10 ** 4:
            return []
        opcode, operand = instructions[i], instructions[i+1]
        match opcode:
            case 0:
                den = 2 ** get_combo(operand)
                A //= den
            case 1:
                B ^= operand
            case 2:
                B = get_combo(operand) % 8
            case 3:
                if A:
                    i = operand
                    continue
            case 4:
                B ^= C
            case 5:
                res.append(get_combo(operand) % 8)
            case 6:
                den = 2 ** get_combo(operand)
                B = A // den
            case 7:
                den = 2 ** get_combo(operand)
                C = A // den
        i += 2
    return res 


def solve():
    A = int(input().split()[-1])
    B = int(input().split()[-1])
    C = int(input().split()[-1])
    input()
    A = 0
    instructions = [int(i) for i in input().split()[-1].split(",")]

    # When B = 0
    for i in range(len(instructions)):
        found = False
        for j in range(8):
            if run(A * 8 + j, B, C, instructions) == instructions[-i-1:]:
                found = True
                A = 8 * A + j
                break
        if not found:
            break
    
    remaining_len = len(instructions) - len(run(A, B, C, instructions))
    for i in range(2 ** (3 * (remaining_len + 1))):
        if run(A * 2 ** (3 * remaining_len) + i, B, C, instructions) == instructions:
            print(A * 2 ** (3 * remaining_len) + i)
            break


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
