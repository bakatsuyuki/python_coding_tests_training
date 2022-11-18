n = int(input())
a = [int(input()) for _ in range(n)]
sushi_count = sum(a)

dp = [[0] * (sushi_count + 1) for _ in range(n + 1)]

dp[0] = a
print(dp)
