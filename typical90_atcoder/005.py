import math

import numpy as np

n, b, k = map(int, input().split())
c = np.array(list(map(int, input().split())))
mod = 10 ** 9 + 7
pow10 = {1: 10 % b}
index = 2
while index <= n / 2:
    before_index = math.floor(index / 2)
    before_value = pow10[before_index]
    pow10[index] = (before_value ** 2) % b
    index *= 2

remainders_count = {}
remainders_count_map = {}
for remainder in c % b:
    if remainder not in remainders_count:
        remainders_count[remainder] = 0
    remainders_count[remainder] += 1

index = 1
counter = 0


def roll(remainders_count, roll_amount):
    upper_remainders_count = {}
    for j in remainders_count:
        count = remainders_count[j]
        new_index = (j * roll_amount) % b
        if new_index not in upper_remainders_count:
            upper_remainders_count[new_index] = 0
        upper_remainders_count[new_index] += count
    return upper_remainders_count


def combine(remainders_count_a, remainders_count_b):
    print('combine')
    new_remainders_count = {}
    for i in remainders_count_a:
        for j in remainders_count_b:
            new_index = (i + j) % b
            if new_index not in new_remainders_count:
                new_remainders_count[new_index] = 0
            new_remainders_count[new_index] += (remainders_count_a[i] * remainders_count_b[j]) % mod
    return new_remainders_count


for index in pow10:
    upper_remainders_count = roll(remainders_count, pow10[index])
    print('こんばいん')
    new_remainders_count = combine(remainders_count, upper_remainders_count)
    remainders_count = new_remainders_count
    remainders_count_map[index] = new_remainders_count


def get_remain_remainder(digits):
    adjusted_digits = 0
    result = 1
    remain_remainders_count = None
    for i in reversed(pow10):
        if digits - adjusted_digits >= i:
            result = (result * pow10[i]) % b
            adjusted_digits += i
            remainder_count = roll(remainders_count_map[i], result)
            if remain_remainders_count is None:
                remain_remainders_count = remainder_count
            else:
                print('こんばいん2')
                combine(remain_remainders_count, remainder_count)
    return remain_remainders_count


remain_digits = n - max(pow10) * 2

print(pow10)
print(remain_digits)
print(combine(remainders_count, roll(get_remain_remainder(remain_digits), max(pow10) ** 2))[0] % mod)

exit()
# print(c_ndarray + np.expand_dims(c_ndarray, -1) * 10 + np.expand_dims(c_ndarray, -1) * 100)
remainders_count = np.zeros(b, dtype=int)
for remainder in c % b:
    remainders_count[remainder] += 1
result_map = {1: remainders_count}

base_remainder = 10 % b
interval = None
for i in range(2, b + 1):
    if base_remainder == (base_remainder ** i) % b:
        interval = i - 1

'''

def dps(digits):
    if digits in result_map:
        return result_map[digits]
    divided_value1 = math.floor(digits / 2)
    divided_value2 = digits - divided_value1
    remainders_count1 = dps(divided_value1)
    remainders_count2 = dps(divided_value2)
    print(divided_value2 - 1)
    reshaped_remainders_count2 = np.roll(remainders_count2, (10 ** (divided_value2 - 1)) % n).reshape((b, 1))
    print(f'{divided_value1}: {remainders_count1}')
    print(f'{divided_value2}: {remainders_count2}')
    result = np.sum(remainders_count1 + reshaped_remainders_count2, axis=0) % mod
    result_map[digits] = result
    return result


print(dps(n))

exit()
'''
print(remainders_count)
for i in range(1, interval):
    new_remainders_count = np.zeros(b, dtype=int)
    for j in range(len(remainders_count)):
        count = remainders_count[j]
        new_index = int((j * base_remainder * i) % b)
        new_remainders_count[new_index] += count
    print(new_remainders_count)
    remainders_count = np.sum(remainders_count + new_remainders_count.reshape((1, b)), axis=0)

base_remainders_count = remainders_count.reshape((1, b))

for i in range(1, math.floor(n / interval)):
    remainders_count = np.sum(remainders_count + base_remainders_count, axis=0)

print(remainders_count)
quit()

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
