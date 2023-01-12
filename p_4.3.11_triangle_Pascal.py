n = int(input())

def calc_line_func(line):
    clc_line = []
    for i in range(len(line)):
        if i == 0:
            clc_line.append(1)
        elif i == len(line):
            clc_line.append(1)
        else:
            clc_line.append(line[i] + line[i - 1])
    clc_line.append(1)
    return clc_line

def func_print_str(lists):
    print(*lists)

def string_eteration_func(n):
    st_line = []
    for i in range(1, n + 1):
        if n == 1:
            st_line = [1]
        else:
            st_line = calc_line_func(st_line)
        func_print_str(st_line)

string_eteration_func(n)



