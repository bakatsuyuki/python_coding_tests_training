n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
min_a = min(a)
dp = [False] * (k + 1)
for i in range(len(dp)):
    if i < min_a:
        continue
    is_win = False
    for j in range(n):
        target = i - a[j]
        if target >= 0 and not dp[target]:
            is_win = True
            break
        if target < 0:
            break

    dp[i] = is_win

print('First' if dp[-1] else 'Second')
