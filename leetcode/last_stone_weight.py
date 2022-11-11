from typing import List

from line_profiler_pycharm import profile


class Solution:
    def __init__(self):
        self.target_weight = None
        self.stones = None
        self.len_stones = None

    @profile
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        self.len_stones = len(stones)
        self.stones = stones
        sum_stones = sum(stones)
        self.target_weight = sum_stones // 2
        group1_weight = self.get_weight(0, 0)
        return abs((sum_stones - group1_weight) - group1_weight)

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


print(Solution().lastStoneWeightII([89, 23, 100, 93, 82, 98, 91, 85, 33, 95, 72, 98, 63, 46, 17, 91, 92, 72, 77]))
print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
# print(Solution().lastStoneWeightII(
#    [89, 23, 100, 93, 82, 98, 91, 85, 33, 95, 72, 98, 63, 46, 17, 91, 92, 72, 77, 79, 99, 96, 55, 72, 24, 98, 79, 93,
#     88, 92]))
