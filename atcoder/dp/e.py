n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
v_list = [wv_child[1] for i, wv_child in enumerate(wv)]
sum_v = sum(v_list)
dp = [[w + 1] * (sum_v + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    current_w, current_v = wv[i - 1]
    for j in range(sum_v + 1):
        if current_v >= j:
            dp[i][j] = min(dp[i - 1][j], current_w)
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - current_v] + current_w)

print(max(i for i, x in enumerate(dp[-1]) if x <= w))
