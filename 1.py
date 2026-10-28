
def binary(a, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == key:
        return mid
    elif a[mid] < key:
        return binary(a, mid + 1, high, key)
    else:
        return binary(a, low, mid - 1, key)

a = list(map(int, input().split()))
key = int(input("enter key "))

i = binary(a, 0, len(a) - 1, key)

if i == -1:
    print("Not found")
else:
    print("Found at index", i)




a = list(map(int, input().split()))
key = int(input())

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Found at index", mid)
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")




a = list(map(int, input().split()))
key = int(input())

for i in range(len(a)):
    if a[i] == key:
        print("Found at index", i)
        break
else:
    print("Not found")
