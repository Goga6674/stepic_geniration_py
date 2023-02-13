cin = input()
dep = int(cin[0])
wid = int(cin[2])

for i in range(dep):
    tmp = []
    for j in range(wid):
        if i % 2 == 0 and j == 0:
            tmp.append('.')
        if i % 2 == 1 and j == 0:
            tmp.append('*')
        if j > 0:
            if tmp[j - 1] == '.':
                tmp.append('*')
            else:
                tmp.append('.')
    print(*tmp)
