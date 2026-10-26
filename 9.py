#tsp
n=int(input("enter the number of cities "))
d=[list(map(int,input().split())) for i in range(n)]
dp={}

def tsp(city,mask):
    if mask==(1 << n)-1:
        return d[city][0]
    
    if(city,mask) in dp:
        return dp[(city,mask)]
    
    ans=999999
    for i in range(n):
        if not mask &(1<<i):
            cost=d[city][i]+tsp(i,mask| (1 << i))
            ans=min(ans,cost)

    dp[(city,mask)]=ans
    return ans

print("min cosst ",tsp(0,1))