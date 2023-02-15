n = int(input())

for i in range(n):
    tmp = []
    for j in range(n):
        if j == n - 1 - i:
            tmp.append(1)
        elif j < n - 1 - i:
            tmp.append(0)
        else:
            tmp.append(2)
    print(*tmp)
