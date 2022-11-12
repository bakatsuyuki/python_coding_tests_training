n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = abc[0]

for i in range(1, n):
    still_before_a = dp[i - 1][0]
    still_before_b = dp[i - 1][1]
    still_before_c = dp[i - 1][2]
    today_a = abc[i][0]
    today_b = abc[i][1]
    today_c = abc[i][2]
    dp[i][0] = today_a + max(still_before_b, still_before_c)
    dp[i][1] = today_b + max(still_before_a, still_before_c)
    dp[i][2] = today_c + max(still_before_a, still_before_b)

print(max(dp[-1]))
