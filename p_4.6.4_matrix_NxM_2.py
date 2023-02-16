cin = input().split()
hig = int(cin[0])
wid = int(cin[1])
arr = []
counter = 0

for i in range(wid):
    tmp = []
    for j in range(hig):
        counter += 1
        tmp.append(counter)
    arr.append(tmp)

for i in range(hig):
    ant = []
    for j in range(wid):
        ant.append(arr[j][i])
    print(*ant)

