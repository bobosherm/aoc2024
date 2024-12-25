import sys
from contextlib import contextmanager
import random


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
    m, k = 90, 313 - 91
    wires = dict()
    for _ in range(m):
        wire, val = input().split(": ")
        val = int(val)
        wires[wire] = 1
    
    input()
    gates = []
    rev_gates = dict()
    for _ in range(k):
        lr, res = input().split(" -> ")
        l, op, r = lr.split()
        l, r = sorted((l, r))
        gates.append((l, r, res, op))
        rev_gates[res] = [l, r, op]
    
    def evaluate():
        for _ in range(k):
            for i in range(k):
                l, r, res, op = gates[i]
                if l in wires and r in wires:
                    if op == "AND":
                        wires[res] = wires[l] & wires[r]
                    elif op == "OR":
                        wires[res] = wires[l] | wires[r]
                    else:
                        wires[res] = wires[l] ^ wires[r]
    
    def set_input(x, y):
        for i in range(45):
            key_x, key_y = 'x' + '0' * (i < 10) + str(i), 'y' + '0' * (i < 10) + str(i)
            wires[key_x] = x % 2
            wires[key_y] = y % 2
            x //= 2
            y //= 2
    
    def check(z, incorrect_bits):
        for i in range(46):
            key = 'z' + '0' * (i < 10) + str(i)
            if wires[key] != z % 2:
                incorrect_bits.add(i)
            z //= 2
        return

    def debug():
        x, y, z = "", "", ""
        for i in range(45):
            key_x, key_y, key_z = 'x' + '0' * (i < 10) + str(i), 'y' + '0' * (i < 10) + str(i), 'z' + '0' * (i < 10) + str(i)
            x += str(wires[key_x])
            y += str(wires[key_y])
            z += str(wires[key_z])
        z += str(wires["z45"])
        print("DEBUG>>>>>>>")
        print(x)
        print(y)
        print(z)
        print("<<<<<<<<<<<<")
        print()

    def tree_view(wire, indent=0, depth=5):
        if indent == 0:
            print(wire)
        if wire[0] in "xy" or depth == 0:
            print(f"{' ' * indent}{wire}")
        else:
            l, r, op = rev_gates[wire]
            print(f"{' ' * indent}{op}")
            tree_view(l, indent+4, depth - 1)
            tree_view(r, indent+4, depth - 1)
        if indent == 0:
            print()
    
    wrong_bits = set()
    for _ in range(10):
        x, y = random.randint(0, 2 ** 45 - 1), random.randint(0, 2 ** 45 - 1)
        # x, y = 2 ** 45 - 1, 2 ** 45 - 1
        set_input(x, y)
        evaluate()
        check(x + y, wrong_bits)
        debug()
    
    print("INCORRECT BITS:")
    print(wrong_bits)
    print()

    #Correct bit, for reference.
    tree_view("z05")
    # Incorrect bits
    tree_view("z35")
    tree_view("z31")
    tree_view("z22")
    tree_view("z14")


# Full adder:
#
# x[i] -----+-----------+
#           |           |
#            > XOR --+   > AND -+
#           |        |  |       |
# y[i] -----+--------|--+        > OR ------> carry[i]
#                    |          |
#                    +--+-------|--+
#                       |       |  |
#                        > AND -+   > XOR --> z[i]
#                       |          |
# carry[i-1] -----------+----------+


# y14 XOR x14 -> ttd
# nhg XOR ttd -> vss
# tfw OR cgt -> z14
# swap vss z14

# y22 AND x22 -> kdh
# y22 XOR x22 -> hjf
# swap kdh hjf

# x31 XOR y31 -> nrr
# nrr AND sms -> z31
# nrr XOR sms -> kpp
# swap kpp z31

# y35 AND x35 -> z35
# y35 XOR x35 -> bbc
# bbc XOR jkb -> sgj
# swap sgj z35


# res: hjf,kdh,kpp,sgj,vss,z14,z31,z35


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
