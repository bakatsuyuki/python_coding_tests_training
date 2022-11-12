from line_profiler_pycharm import profile


@profile
def solve(n, k, h):
    dp = [0] * n
    for i in range(1, n):
        results = []
        for j in range(1, min(i + 1, k + 1)):
            results.append(dp[i - j] + abs(h[i] - h[i - j]))
        dp[i] = min(results)
    return dp[-1]


n, k = map(int, input().split())
h = list(map(int, input().split()))
print(solve(n, k, h))
