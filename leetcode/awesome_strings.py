import numpy as np
from line_profiler_pycharm import profile


class Solution:
    @profile
    def longestAwesome(self, s: str) -> int:
        all_numbers_counts = [0] * 10
        len_s = len(s)
        s_int = list(map(int, list(s)))
        dp = np.zeros((len_s, 10), dtype=bool)
        min_result = 0
        for i in range(len_s):
            s_child = s_int[i]
            all_numbers_counts[s_child] += 1
            if i > 0:
                dp[i] = dp[i - 1]
            dp[i][s_child] = not dp[i][s_child]
            if self.oddCount(dp[i]) < 2:
                min_result = i + 1
        for i in range(len_s):
            if len_s - i - 1 < min_result:
                break
            current_dp = dp[len_s - 1] != dp[i]
            odd_count = self.oddCount(current_dp)
            for j in reversed(range(i + min_result, len_s)):
                if odd_count < 2:
                    min_result = j - i
                    break

                if current_dp[s_int[j]]:
                    odd_count -= 1
                else:
                    odd_count += 1
                current_dp[s_int[j]] = not current_dp[s_int[j]]

        return min_result

    def oddCount(self, occurrences):
        return np.count_nonzero(occurrences)


print(Solution().longestAwesome(
    '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'))
