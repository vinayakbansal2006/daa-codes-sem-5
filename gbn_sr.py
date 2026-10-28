n = int(input("Frames: "))
w = int(input("Window size: "))
lost = list(map(int, input("Lost frames: ").split()))

base = 1
sent = 0

while base <= n:
    end = min(base + w - 1, n)
    sent += end - base + 1

    print("Sent:", base, "to", end)

    x = next((i for i in sorted(lost) if base <= i <= end), None)

    if x:
        print("Frame", x, "lost. Go back to", x)
        sent += end - x + 1
        base = x
        lost.remove(x)
    else:
        base = end + 1

print("Total transmissions:", sent)