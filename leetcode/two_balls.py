import math
from typing import List

from line_profiler_pycharm import profile


class Solution:
    @profile
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_result = (position[-1] - position[0] // (m - 1))
        min_result = 0
        while max_result > min_result:
            distance = math.ceil((max_result + min_result) / 2)
            if self.validation(position, m, distance):
                min_result = distance
            else:
                max_result = distance - 1
        return max_result

    @profile
    def validation(self, position, m, distance):
        count = 0
        before_position = -distance
        for current_position in position:
            if current_position >= before_position + distance:
                count += 1
                before_position = current_position
                if count >= m:
                    return True
        return False


print(Solution().maxDistance(
    position=[269826447, 974181916, 225871443, 189215924, 664652743, 592895362, 754562271, 335067223, 996014894,
              510353008, 48640772, 228945137, 2698216447, 9741811916, 2258711443, 1892159124, 6646512743, 5928915362,
              7545162271, 3350167223, 9960114894,
              5103513008, 486407712, 2289451371], m=3))
