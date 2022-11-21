import sys

from line_profiler_pycharm import profile

n = int(input())
sys.setrecursionlimit(n * 10)
a = list(map(int, input().split()))
sushi_count = sum(a)

dp = [[[None for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

default_c1 = len([x for _, x in enumerate(a) if x == 1])
default_c2 = len([x for _, x in enumerate(a) if x == 2])
default_c3 = len([x for _, x in enumerate(a) if x == 3])
dp[0][0][0] = 0


@profile
def solve(c1, c2, c3):
    if dp[c1][c2][c3] is not None:
        return dp[c1][c2][c3]

    denominator = 1
    if c1 > 0:
        denominator += solve(c1 - 1, c2, c3) * c1 / n
    if c2 > 0:
        denominator += solve(c1 + 1, c2 - 1, c3) * c2 / n
    if c3 > 0:
        denominator += solve(c1, c2 + 1, c3 - 1) * c3 / n
    c0 = n - c1 - c2 - c3
    p0 = c0 / n
    result = denominator / (1 - p0)
    dp[c1][c2][c3] = result
    return result


print(solve(default_c1, default_c2, default_c3))
