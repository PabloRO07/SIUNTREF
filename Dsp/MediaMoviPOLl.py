import numpy as np

x = [1, 1, 1, 2, 1, 1, 1, 1, 1, 1]
M = 3
y = np.zeros(len(x))
q = 0
m = M
# for i in range(len(x)):
#     y[i] = np.sum(x[q:m])/M
#     q = q + 1
#     m = m + 1
# print(y)

for i in range(len(x)):
    if i == 0:
        y[i] = np.sum(x[i:M])
    elif i+1 < len(x):
        print(i)
        y[i] = y[i-1] - x[i-1] + x[i-1+m]
print(y)
