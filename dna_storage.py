from operator import index

t = int(input())

while t > 0:
    n = int(input())
    s = input()
    l = list(s)
    dna_codes = {'00':'A','01':'T','10':'C','11':'G'}
    i = 0
    while i < len(l):
        code = l[i] + l[i+1]
        print(dna_codes.get(code),end='')
        code = ''
        i += 2
    print("")
    t -= 1