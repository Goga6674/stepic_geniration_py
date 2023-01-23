# reading size
n = int(input())

# func read strings and maeke lists - matrix
def matrix(n):
    matrix = []
    m_string = []
    for i in range(n):
        st = input()
        m_string = st.split()
        matrix.append(m_string)
        m_string = []
    return matrix

# find max num in main_diagon
def find_max(a):
    tmp = -10000
    flag = 0
    for i in range(n):
        for j in range(n):
            if j <= i and int(a[i][j]) >= tmp:
                tmp = int(a[i][j])
                flag += 1
    if flag == 0:
        tmp = 0
    return tmp

print(find_max(matrix(n)))
