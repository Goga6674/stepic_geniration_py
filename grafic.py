import matplotlib.pyplot as plt
from math import cos, log, sin, e, degrees, pow

x = int(input())

def f_x(x):
    tmp = pow(e, cos(x)) + log(pow(sin(0.8 * x), 2) + 1, 10) * cos(x)
    
    return degrees(tmp)

def y_x(x):
    tmp = -log(pow(cos(x) + sin(x), 2), 10) + 2
    
    return degrees(tmp)

# make interval
a = -240
b = 360
n = 50
h = (b - a) / (n - 1)

# make lists of argumets
x_list = [a + h * i for i in range(n)]
f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]
# make line`s 
line_f = plt.plot(x_list, f_list, label="f(x)")
line_y = plt.plot(x_list, y_list, label="y(x)")
# set styls of lines
plt.setp(line_f, color="blue", linewidth=2)
plt.setp(line_y, color="red", linewidth=2)
# set axis 
#plt.gca().spines["left"].set_position('zero')
#plt.gca().spines["bottom"].set_position('zero')
#plt.gca().spines["top"].set_visible(False)
#plt.gca().spines["right"].set_visible(False)
# set legend
plt.legend()
plt.title("Графики функций")
# print all
plt.show()

print(*x_list)
print()
print(*f_list)
print()
print(*y_list)
