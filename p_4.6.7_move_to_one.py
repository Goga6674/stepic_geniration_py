cin = input().split()
hig = int(cin[0])
wid = int(cin[1])
row = [1 + i for i in range(wid)]
save = 1

for i in range(hig):
    print(*row)
    tmp = row.pop(0)
    row.append(tmp)
