#read num of ctrings
n = int(input()) # n - strings

#read num 0f colomms
m = int(input()) # m - rows

#read words
matrix = []
colom = []
st = ""

for i in range(n):
    for j in range(m):
        colom.append(input())
    matrix.append(colom)
    colom = []
    
#print(first matrix)
for i in range(n):
    print(*matrix[i])
    
# free string
print()

#output second matrix
for i in range(m):
    for j in range(n):
        st += matrix[j][i] + ' '
    print(st)
    st = ''
