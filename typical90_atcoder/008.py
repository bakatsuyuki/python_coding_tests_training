from copy import deepcopy

import numpy as np

n = int(input())
s = input()

mod = 10 ** 9 + 7

target_chars = 'atcoder'

indexes = [[i for i, x in enumerate(s) if x == target_chars[index]] for index in range(len(target_chars))]


def remove_errors_from_indexes(indexes):
    has_changed = False
    copied_indexes = deepcopy(indexes)
    for i in range(len(target_chars)):
        for j in range(len(indexes[i])):
            index = indexes[i][j]
            if i < len(indexes) - 1 and index > max(indexes[i + 1]):
                has_changed = True
                print('削除1')
                print(f'i: {i}')
                print(index)
                print(indexes[i + 1])
                del (copied_indexes[i][j])
            elif i > 0 and index < min(indexes[i - 1]):
                has_changed = True
                print('削除2')
                print(f'i: {i}')
                print(index)
                print(indexes[i - 1])
                # コピーしてるからindexずれてる
                # それのせいでバグってる
                del (copied_indexes[i][j])
    if has_changed:
        return remove_errors_from_indexes(copied_indexes)
    else:
        return copied_indexes


indexes = remove_errors_from_indexes(indexes)

dp = np.array([[0] * n] * len(target_chars))

for i in range(len(indexes)):
    for j in indexes[i]:
        if i == 0:
            dp[i][j:] += 1
        elif dp[i - 1][j] != 0:
            dp[i][j:] = (dp[i][j:] + dp[i - 1][j:]) % mod

print(dp)
print(dp[len(target_chars) - 1][n - 1])
