def merge(a):
  if len(a)<=1:
    return a
  
  m=len(a)//2
  l=merge(a[:m])
  r=merge(a[m:])
  
  c=[]
  while l and r:
    if l[0]<r[0]:
      c.append(l.pop(0))
    else:
      c.append(r.pop(0))

    return c+l+r

a=list(map(int,input("enter the values ").split()))
print(merge(a))