# read n and matrix
def matrix_sqr():
    matrix = [input().split() for _ in range(int(input()))]
    return matrix

# condition area
def condition(i, j):
    if i < j and i < n - 1 - j: # UP
        return 0
    elif i < j and i > n - 1 - j: # right
        return 1
    elif i > j and i > n - 1 - j: # down
        return 2
    elif i > j and i < n - 1 -j: # left
        return 3

# sortt and calculating
def sort(a):
    sum_u = 0
    sum_r = 0
    sum_d = 0
    sum_l = 0
    for i in range(n):
        for j in range(len(a[i])):
            if condition(i, j) == 0:
                sum_u += int(a[i][j])
            elif condition(i, j) == 1:
                sum_r += int(a[i][j])
            elif condition(i, j) == 2:
                sum_d += int(a[i][j])
            elif condition(i, j) == 3:
                sum_l += int(a[i][j])

    tmp = [sum_u, sum_r, sum_d, sum_l]
    return tmp

matrix = matrix_sqr()
n = len(matrix)

arr = sort(matrix)

print("Верхняя четверть:", arr[0])
print("Правая четверть:", arr[1])
print("Нижняя четверть:", arr[2])
print("Левая четверть:", arr[3])
