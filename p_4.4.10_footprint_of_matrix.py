# reading size
n = int(input())

# reading matrix
matrix_st = []
m_string = []
for i in range(n):
    st = input()
    m_string = st.split()
    matrix_st.append(m_string)
    m_string = []

# sum
sum_ = 0

for i in range(n):
    for j in range(n):
        if i == j:
            sum_ += int(matrix_st[i][j])

print(sum_)



