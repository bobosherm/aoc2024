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
    # Plz don't read
    inp = input()
    disk = ["?"]
    pos = 0
    fid = 0
    for i in range(len(inp)):
        l = int(inp[i])
        if i % 2 == 0:
            disk += [str(fid)] * l
            fid += 1
        else:
            disk += ["."] * l
        pos += l
    disk.append(".")
    prev = "invalid"
    r = len(disk) - 1
    rc = 0
    while r >= 0:
        if disk[r] == prev:
            rc += 1
        else:
            if prev != "invalid":
                l = 0
                lc = 0
                while l < r:
                    if disk[l] == ".":
                        lc += 1
                        if lc >= rc:
                            for i in range(rc):
                                disk[l-i] = disk[r+i+1]
                                disk[r+i+1] = "."
                            break
                    else:
                        lc = 0
                    l += 1
                
            if disk[r] != ".":
                rc = 1
                prev = disk[r]
            else:
                rc = 0
                prev = "invalid"
        r -= 1
    disk = disk[1:-1]
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += i * int(disk[i])
    print(checksum)



def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
