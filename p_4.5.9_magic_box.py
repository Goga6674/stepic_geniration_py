arr = [input().split() for _ in range(int(input()))]
n = len(arr)

flag = 0
midl_a = 0
test = []
for i in range(1, n**2):
    test.append(i)
print(test)

for i in range(n):
    for j in range(n):
        arr[i][j] = int(arr[i][j])
        midl_a += arr[i][j]
        for k in range(n**2):
            if test[k] == arr[i][j]:
                test.pop(k)
            else:
                flag += 1
if midl_a / (n * n) == arr[i][j]:
    flag += 1
# функция проверки суммы сторк
def chec_str(str, et):
    test = sum(str)
    if test == et:
        return True
    else:
        return False

# функция создания и проверки столбцев
def meck_col(arr, c):
    tmp = 0
    for i in range(n):
        for j in range(n):
            if j == c:
                tmp += arr[i][j]
    if tmp == et:
        return True
    else:
        return False

# функция созания и проверки главной диагонали
def meck_di(arr, et):
    tmp = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                tmp += arr[i][j]
    if tmp == et:
        return True
    else:
        return False

# функция сoздания и проверки побочной диагонали
def mack_po(arr, et):
    tmp = 0
    for i in range(n):
        for j in range(n):
            if j == n - i - 1:
                tmp += arr[i][j]
    if tmp == et:
        return True
    else:
        return False

# etalon значение для сравнения строк, столбцев и диагоналей
et = sum(arr[0])

for i in range(n):
    if chec_str(arr[i], et): # для строк
        pass
    else:
        flag += 1
        break
    if meck_col:
        pass
    else:
        flag += 1
    if meck_di(arr, et):
        pass
    else:
        flag += 1
        break
    if mack_po(arr, et):
        pass
    else:
        flag += 1
        break

if flag == 0:
    print("YES")
else:
    print("NO")
