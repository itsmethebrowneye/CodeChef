t = int(input())
while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    final_cost = 0

    for i, elem in enumerate(a):
        if elem >= x:
            final_cost += b[i]

    print(final_cost)

    t -= 1
