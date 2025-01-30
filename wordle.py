t = int(input())

while t > 0:
    S = input()
    T = input()
    length = len(S)
    i = 0
    while i < length:
        if S[i] != T[i]:
            print("B", end='')
        else:
             print("G", end='')
        i += 1
    print("")
    t -= 1
