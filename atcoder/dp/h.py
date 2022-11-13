h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]

dp[0][0] = 1
mod = 10 ** 9 + 7

for i in range(0, h):
    for j in range(0, w):
        current_point = a[i][j]
        if current_point == '#':
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= mod

print(dp[-1][-1])
