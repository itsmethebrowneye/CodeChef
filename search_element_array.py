a, b = map(int,input().split())
arr = map(int, input().split())
available = False
for elem in arr:
    if elem == b: available = True

if available:
    print("Yes")
else:
    print("No")