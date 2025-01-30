
t = int(input())

while t > 0:
    arr = list(map(int,input().split()))
    s = sorted(arr,reverse=True)
    if len(s) > 1:
        print(s[1])
    else:
        print(s[0])

    t-=1