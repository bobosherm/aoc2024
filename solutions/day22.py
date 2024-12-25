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
    n = 2474
    steps = 2000
    M = 16777216
    seq_profit = dict()
    
    for _ in range(n):
        buyer_seq_profit = {}
        secret = int(input())
        price_changes = []

        for _ in range(steps):
            old_secret = secret
            secret = ((secret * 64) ^ secret) % M
            secret = ((secret // 32) ^ secret) % M
            secret = ((secret * 2048) ^ secret) % M
            price_changes.append((secret % 10 - old_secret % 10, secret % 10))
        
        for i in range(3, steps):
            key = f"{price_changes[i-3][0]}_{price_changes[i-2][0]}_{price_changes[i-1][0]}_{price_changes[i][0]}"
            if key not in buyer_seq_profit:
                buyer_seq_profit[key] = price_changes[i][1]

        for key, value in buyer_seq_profit.items():
            seq_profit[key] = seq_profit.get(key, 0) + value
    
    print(max(seq_profit.values()))
 
 
def main():
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
