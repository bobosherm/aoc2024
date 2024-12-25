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


def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[j] not in graph[nodes[i]]:
                return False
    return True


def solve():
    n = 3380
    edges = [input().split("-") for _ in range(n)]
    graph = {}
    for a, b in edges:
        if graph.get(a) is not None:
            graph[a].add(b)
        else:
            graph[a] = set([b])
        if graph.get(b) is not None:
            graph[b].add(a)
        else:
            graph[b] = set([a])
    
    max_clique = []

    def backtrack(curr_clique, start):
        nonlocal max_clique
        if len(curr_clique) > len(max_clique):
            max_clique = curr_clique
            print(">>", len(max_clique), ",".join(sorted(max_clique)))

        for i in range(start, len(graph)):
            node = list(graph.keys())[i]
            if is_clique(graph, curr_clique + [node]):
                backtrack(curr_clique + [node], i + 1)

    backtrack([], 0)
    print(",".join(sorted(max_clique)))


def main():
    enable_fileio = 0
    enable_fileio = 1
    with fileio(enable_fileio):
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()


main()
