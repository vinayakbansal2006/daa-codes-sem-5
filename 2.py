def quick(a):
    if len(a) <= 1:
        return a

    p = a[0]
    l = [x for x in a[1:] if x <= p]
    r = [x for x in a[1:] if x > p]

    return quick(l) + [p] + quick(r)

a = list(map(int, input().split()))
print(quick(a))