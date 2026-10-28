#kruskal algo
n = int(input("Enter number of vertices: "))
g = [list(map(int, input().split())) for i in range(n)]

edges = []

for i in range(n):
    for j in range(i + 1, n):
        if g[i][j] > 0:
            edges.append((g[i][j], i, j))

edges.sort()

parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

count = 0

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, ":", w)
        parent[a] = b
        count += 1

        if count == n - 1:
            break

if count != n - 1:
    print("Graph is disconnected")
