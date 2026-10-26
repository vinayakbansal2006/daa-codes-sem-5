
#prims algortim
n=int(input("enter number of vertices "))
g=[list(map(int,input().split()))for i in range(n)]

visited=[False]*n
visited[0]=True
edges=0

while edges<n-1:
    minimum=999
    x=y=-1
    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and g[i][j] >0:
                    if g[i][j]<minimum:
                        minimum=g[i][j]
                        x,y=i,j
    if y==-1:
        print("graph is disconnected ")
        break
    print(x,"-",y," : ",minimum)
    visited[y]=True
    edges += 1
    