c, r, n = map(int, input().split())
p = list(map(int, input().split()))
b = 0

for x in p:
    if b + x <= c:
        b += x
        d = 0
    else:
        d = x

    s = min(b, r)
    b -= s
    print("Sent:", s, "Left:", b, "Dropped:", d)

while b > 0:
    s = min(b, r)
    b -= s
    print("Sent:", s, "Left:", b)