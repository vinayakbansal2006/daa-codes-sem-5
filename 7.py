#activity selection
n = int(input("Enter number of activities: "))
s = list(map(int, input("Enter start times: ").split()))
f = list(map(int, input("Enter finish times: ").split()))

a = sorted(zip(s, f), key=lambda x: x[1])

count = 1
last = a[0][1]

print(a[0])

for i in range(1, n):
    if a[i][0] >= last:
        print(a[i])
        count += 1
        last = a[i][1]

print("Total activities:", count)
