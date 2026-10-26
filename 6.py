
#fractional knapsack
n=int(input("enter number of items "))
w=list(map(int,input("enter weights: ").split()))
v=list(map(int,input("enter values: ").split()))
c=int(input("enter capacity: "))

items=sorted(zip(w,v),key = lambda x: x[1]/x[0],reverse=True)
profit=0

for weight,value in items:
  if c>=weight:
    profit += value
    c-= weight
  else:
    profit += value*c/weight
    break

print("max profit ",profit)