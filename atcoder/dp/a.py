n = int(input())
h = list(map(int, input().split()))
dp = [0] * n
dp[0] = 0
dp[1] = abs(h[0] - h[1])
for i in range(2, n):
    current_h = h[i]
    before_h = h[i - 1]
    before_h2 = h[i - 2]
    dp[i] = min(dp[i - 1] + abs(current_h - before_h), dp[i - 2] + abs(current_h - before_h2))

print(dp[-1])
