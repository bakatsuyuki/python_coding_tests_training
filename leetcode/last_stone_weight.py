from typing import List

from line_profiler_pycharm import profile


class Solution:
    @profile
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        sum_stones = sum(stones)
        target_weight = sum_stones // 2
        dp = [[0] * (target_weight + 1) for _ in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1):
            stone = stones[i - 1]
            dp[i][0:stone] = dp[i - 1][0:stone]
            for j in range(stone, target_weight + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stone] + stone)

        return abs((sum_stones - dp[-1][-1]) - dp[-1][-1])

    @profile
    def get_weight(self, currentWeight, index):
        if index >= self.len_stones:
            return currentWeight
        current_stone = self.stones[index]
        if current_stone + currentWeight > self.target_weight:
            return currentWeight
        new_index = index + 1
        return max(
            self.get_weight(currentWeight + current_stone, new_index),
            self.get_weight(currentWeight, new_index),
        )


for _ in range(100):
    print(Solution().lastStoneWeightII([89, 23, 100, 93, 82, 98, 91, 85, 33, 95, 72, 98, 63, 46, 17, 91, 92, 72, 77]))
    print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
