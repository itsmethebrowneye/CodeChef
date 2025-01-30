t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    largest = arr[0]
    for elem in arr:
        if elem > largest: largest = elem
    print(largest)
    t -= 1
