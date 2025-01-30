t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    happy = 0;

    i = 0
    while n > 0:
        if a[i] < b[i]:
            if a[i] * 2 >= b[i]:
                happy += 1;
        else:
            if b[i] * 2 >= a[i]:
                happy += 1
        i += 1
        n -= 1

    print(happy)
