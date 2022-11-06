import numpy as np

n = int(input())
s = input()

mod = 10 ** 9 + 7

target_chars = 'atcoder'

s = [x for i, x in enumerate(s) if x in target_chars]

indexes = [[i for i, x in enumerate(s) if x == target_chars[index]] for index in range(len(target_chars))]
dp = np.array([[0] * (len(s))] * (len(target_chars) + 1))


def error_check():
    if not all(indexes):
        print('0')
        exit()


for i in range(len(indexes) - 1):
    next_i = i + 1
    indexes[next_i] = [index for _, index in enumerate(indexes[next_i]) if index > min(indexes[i])]
    error_check()

    reverse_i = len(indexes) - 1 - i
    before_reverse_i = reverse_i - 1
    indexes[before_reverse_i] = [index for _, index in enumerate(indexes[before_reverse_i]) if
                                 index < max(indexes[reverse_i])]
    error_check()

dp[0] = 1
for raw_i in range(len(indexes)):
    index = indexes[raw_i]
    i = raw_i + 1
    for j in range(len(s)):
        if j in index:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % mod
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[-1][-1])
# print(dp[len(target_chars) + 1][n] % mod)
