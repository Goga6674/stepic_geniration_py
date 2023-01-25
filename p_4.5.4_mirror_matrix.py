# reading matrix
def matrix_sqr():
    matrix = [input().split() for _ in range(int(input()))]
    return matrix

# condition area
def condition(arr, i, j):
    teset_str = ''
    if i != j:
        if arr[i][j] == arr[j][i]:
            teset_str = "YES"
        else:
            teset_str = "NO"
    return teset_str

matrix = matrix_sqr()
line = ''
for i in range(len(matrix)):
    for j in range(len(matrix)):
        line += condition(matrix, i, j)

if 'NO' in line:
    print('NO')
else:
    print("YES")
