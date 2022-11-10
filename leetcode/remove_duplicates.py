from collections import deque

from line_profiler_pycharm import profile

duplicates = {f'{chr(i)}{chr(i)}' for i in range(97, 123)}


class Solution:
    @profile
    def removeDuplicates(self, s: str) -> str:
        result = deque()
        for single_s in list(s):
            if result and result[-1] == single_s:
                result.pop()
            else:
                result.append(single_s)
        return ''.join(result)

    @profile
    def removeDuplicatesOld(self, s: str) -> str:
        result = deque()
        for single_s in list(s):
            if result and result[-1] == single_s:
                result.pop()
            else:
                result.append(single_s)
        return ''.join(result)


t = input()
for i in range(30):
    print(Solution().removeDuplicates(t))
    print(Solution().removeDuplicatesOld(t))
