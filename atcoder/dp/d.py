n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    current_w, current_v = wv[i - 1]
    for j in range(w + 1):
        if current_w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - current_w] + current_v)

print(dp[-1][-1])
