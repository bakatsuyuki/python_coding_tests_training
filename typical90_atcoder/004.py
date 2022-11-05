import numpy as np


h, w = map(int, input().split())
a_list = [list(map(int, input().split())) for i in range(h)]
a = np.array(a_list)
x_sum = a.sum(axis=1)
y_sum = a.sum(axis=0)
result = y_sum + x_sum.reshape((len(x_sum), 1)) - a

for line in result:
    print(*line)