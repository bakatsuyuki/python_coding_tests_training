import numpy as np

n, b, k = map(int, input().split())
c = np.array(list(map(int, input().split())))
mod = 10 ** 9 + 7
# print(c_ndarray + np.expand_dims(c_ndarray, -1) * 10 + np.expand_dims(c_ndarray, -1) * 100)
remainders_count = np.zeros(b, dtype=int)
for remainder in c % b:
    remainders_count[remainder] += 1

for j in range(1, n):
    digit = 10 ** j
    second_remainders_count = np.zeros(b, dtype=int)
    for remainder in c * digit % b:
        second_remainders_count[int(remainder)] += 1
    new_remainders = np.zeros(b, dtype=int)
    for i in range(b):
        new_remainders += np.roll(remainders_count, i) * second_remainders_count[i]
    remainders_count = new_remainders
    remainders_count % mod

print(remainders_count[0] % mod)
'''
for i in range(1, n):
    new_remainders_count = np.zeros(10, dtype=int)
    for current_digit_remainder in (c * pow(10, i)) % b:
        for old_remainder in range(len(remainders_count)):
            if old_remainder == 0:
                continue
            count = remainders_count[old_remainder] % mod
            new_remainder = (old_remainder + current_digit_remainder) % b
            new_remainders_count[new_remainder] += count
    remainders_count = new_remainders_count
    print(new_remainders_count)

print(remainders_count[0] % mod)
'''
