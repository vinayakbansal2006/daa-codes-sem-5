
# dijakstra algoritm
n=int(input("enter the number of vertices "))
g=[list(map(int,input().split())) for i in range(n)]

d=[999]*n
d[0]=0
visited=[False]*n

for i in range(n):
  u=-1
  for j in range(n):
    if not visited[j] and (u==-1 or d[j]<d[u]):
      u=j
  visited[u]=True

  for v in range(n):
    if g[u][v] >0 and not visited[v]:
      if d[u]+g[u][v] <d[v]:
        d[v]=d[u]+g[u][v]
print(d)