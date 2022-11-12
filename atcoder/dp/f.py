from line_profiler_pycharm import profile


@profile
def solve(s, t):
    if s in t:
        return s
    if t in s:
        return t
    last_dp = [''] * (len(t) + 1)
    for i in range(1, len(s) + 1):
        current_dp = [x for _, x in enumerate(last_dp)]
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                current_dp[j] = last_dp[j - 1] + s[i - 1]
            elif len(last_dp[j]) <= len(current_dp[j - 1]):
                current_dp[j] = current_dp[j - 1]
        last_dp = current_dp
    return last_dp[-1]


s = input()
t = input()

print(solve(s, t))
