n = int(input())
dcs = [list(map(int, input().split())) for _ in range(n)]
dcs.sort()

max_d = max([d for d, _, _ in dcs])

dp = [[0 for j in range(max_d + 1)] for i in range(n)]

for i in range(len(dp)):
    d, c, s = dcs[i]
    for j in range(1, len(dp[i])):
        if d < j:
            break
        current_s = s if c <= j else 0
        additional_s = dp[i - 1][j - c] if i - 1 >= 0 and j - c >= 0 else 0
        compare_s1 = dp[i - 1][j] if i - 1 >= 0 else 0
        compare_s2 = dp[i][j - 1] if j - 1 >= 0 else 0
        dp[i][j] = max([current_s + additional_s, compare_s1, compare_s2])

print(int(dp[-1][-1]))
