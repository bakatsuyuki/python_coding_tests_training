import sys

n = int(input())
sys.setrecursionlimit(n * 10)
p = list(map(float, input().split()))
len_p = len(p)
memo = {}

min_forward_count = len_p // 2 + 1

adjust = 10 ** 9
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    forward_p = p[i - 1]
    back_p = 1 - forward_p
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] * back_p
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * forward_p

print(sum(dp[-1][min_forward_count:]))
