n = int(input())

for i in range(n):
    tmp = []
    for j in range(n):
        if i >= j or j <= n - i -1:
            tmp.append(1)
        else:
            tmp.append(0)
    print(*tmp)
