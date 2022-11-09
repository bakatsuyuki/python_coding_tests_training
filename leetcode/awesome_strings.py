from line_profiler_pycharm import profile


class Solution:
    @profile
    def longestAwesome(self, s: str) -> int:
        result = 0
        index_map = [[] for _ in range(10)]
        s_int = list(map(int, list(s)))
        for i in range(len(s_int)):
            index_map[s_int[i]].append(i)
        odds = self.odd_values(s_int)
        queue = []
        if len(odds) < 2:
            return len(s)
        for i in range(len(odds)):
            if len(index_map[i]) > 0:
                queue.append([index_map[i][0], len(s_int) - 1])
                queue.append([0, index_map[i][-1]])

        while queue:
            start, end = queue.pop(0)
            if end - start < result:
                continue
            odds = self.odd_values(s_int[start:end])
            if len(odds) < 2:
                result = end - start
                continue
            for i in range(len(odds)):
                new_indexes = [x for index, x in enumerate(index_map[i]) if start < index < end]
                if len(new_indexes) > 0:
                    queue.append([new_indexes[0], end])
                    queue.append([start, new_indexes[-1]])
        return result

    def odd_values(self, s_int):
        count = [False] * 10
        for s_value in s_int:
            count[s_value] = not count[s_value]
        return [i for i, x in enumerate(count) if x]


print(Solution().longestAwesome('213123'))

# テスト
# print(len(Solution().odd_values([2, 1, 3, 1, 2, 3])) == 0)
# print(len(Solution().odd_values([1, 2, 3, 4, 5, 6, 7, 8])) == 8)
