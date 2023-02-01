arr = [input().split() for _ in range(int(input()))]

n = len(arr)
for i in range(n):
    for j in range(n):
            if i == j:
                arr[i][i], arr[n - 1- i][i] = arr[n - 1- i][i], arr[i][i]
            if j == n - i - 1:
                arr[i][n - 1 - i], arr[i][j] = arr[i][j], arr[i][n - 1 - i]

for i in range(n):
    print(*arr[i])
