t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    minimum = min(a)
    operations = 0
    for elem in a:
        if elem!=minimum:
            operations+=1
    print(operations)