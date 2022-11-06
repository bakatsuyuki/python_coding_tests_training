import numpy as np

n = int(input())
x = np.array([list(map(int, input().split())) for _ in range(n)])


def calc_angle(vec_1, vec_2):
    length_vec_a = np.linalg.norm(vec_1)
    length_vec_c = np.linalg.norm(vec_2)
    inner_product = np.inner(vec_1, vec_2)
    cos = inner_product / (length_vec_a * length_vec_c)
    rad = np.arccos(cos)
    return np.rad2deg(rad)


max_angle = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            max_angle = max(calc_angle(x[i] - x[k], x[j] - x[k]), max_angle)

print(max_angle)
