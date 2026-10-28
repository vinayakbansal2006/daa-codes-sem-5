# hamilton cycle
def solve(path, pos, n, graph):
    if pos == n:
        return graph[path[n-1]][path[0]] == 1

    for v in range(1, n):
        if v not in path and graph[path[pos-1]][v] == 1:
            path[pos] = v

            if solve(path, pos+1, n, graph):
                return True

            path[pos] = -1

    return False


n = int(input("no of vertices"))
graph = [list(map(int, input().split())) for i in range(n)]

path = [-1] * n
path[0] = 0

if solve(path, 1, n, graph):
    print(path + [path[0]])
else:
    print("No Hamiltonian cycle")
