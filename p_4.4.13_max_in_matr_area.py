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

# condition a
def condition(i, j, n):
    if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
        return True
    else:
        return False 

# find aria num
def area_num(a):
    tmp = []
    for i in range(n):
        for j in range(n):
            if condition(i, j, n):
                tmp.append(int(a[i][j]))
    #print(tmp)
    print(max(tmp))

area_num(matrix(n))
