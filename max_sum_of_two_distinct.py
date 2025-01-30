t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    new_arr = sorted(set(a), reverse = True)
    if len(new_arr)<2:
        print(new_arr[0])
    else:
        print(new_arr[0]+new_arr[1])
