t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    non_decreasing = True
    length = len(d)
    i = 0
    while i <= length - 2:
        if d[i] > d[i + 1]:
            print("No")
            non_decreasing = False
            break
        i += 1

    if non_decreasing:
        print("Yes")
    t -= 1
