cin = input().split()
hig = int(cin[0])
wid = int(cin[1])
counter = 0
for i in range(hig):
    tmp = ''
    for j in range(wid):
        counter += 1
        tmp += (str(counter)) + ' '
    print(tmp)
