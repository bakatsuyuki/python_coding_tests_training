import numpy as np

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
print(np.sum(abs(np.array(a) - np.array(b))))
