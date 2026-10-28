#graph colouring
def color(v):
    if v == n:
        print(c)
        return

    for col in range(1, m+1):
        safe = True

        for i in range(n):
            if g[v][i] == 1 and c[i] == col:
                safe = False

        if safe:
            c[v] = col
            color(v+1)
            c[v] = 0

n = int(input("Enter vertices: "))
m = int(input("Enter colors: "))

g = [list(map(int, input().split())) for i in range(n)]

c = [0]*n
color(0)
